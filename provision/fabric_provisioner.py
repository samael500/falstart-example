import os
import fabric

from fabric.api import run, sudo, cd

fabric.state.env.colorize_errors = True
fabric.state.output['stdout'] = False

# task const variables
VARS = dict(
    current_user=fabric.state.env.user,

    # project settings
    project_name='falstartexample',
    user_data=dict(
        username='root',
        email='root@e.co',
        password='123123'
    ),

    # dirs configs
    templates_dir='./provision/templates',
    root_dir='/home/vagrant/proj',
    venv_path='/home/vagrant/venv',
    base_dir='/home/vagrant',

    # nginx config
    http_host='10.1.1.123',
    http_port='80',

    # database config
    db_name='falstartexample',
    db_password='mDwDNmTRZ',
    db_user='falstartexample_user',

    # locale conf
    locale='ru_RU',
    encoding='UTF-8',
)


def sentinel(sentinel_name):
    def sentinel_wrapp(function):
        def wrapped():
            sentinel_path = '/usr/{}'.format(sentinel_name)
            if fabric.contrib.files.exists(sentinel_path):
                fabric.utils.warn('skip {}'.format(sentinel_name))
                return
            function()
            sudo('touch {}'.format(sentinel_path))
        return wrapped
    return sentinel_wrapp


def common():
    """ Common tasks """
    locale()
    apt_packages()
    python_packages()


def nginx():
    """ Install nginx tasks """
    # install nginx
    sudo('apt-get -y install nginx')
    # create nginx config file for project
    fabric.contrib.files.upload_template(
        'nginx-host.j2', '/etc/nginx/sites-available/{project_name}'.format(**VARS),
        context=VARS, use_jinja=True, backup=False, use_sudo=True, template_dir=VARS['templates_dir'])
    # make s-link to enabled sites
    sudo('ln -sf /etc/nginx/sites-available/{project_name} /etc/nginx/sites-enabled/{project_name}'.format(**VARS))
    # restart nginx
    sudo('service nginx restart')


def database():
    """ Install database """
    # install postgres apt
    sudo('apt-get -y install postgresql postgresql-server-dev-all python-psycopg2')
    # make postgers password
    with fabric.context_managers.settings(warn_only=True):
        commands = (
            'CREATE USER {db_user};',
            'ALTER USER {db_user} WITH PASSWORD \'{db_password}\';',
            'ALTER USER {db_user} CREATEDB;',
            'CREATE DATABASE {db_name};',
            'GRANT ALL PRIVILEGES ON DATABASE {db_name} TO {db_user};',
        )
        for command in commands:
            run('sudo -u postgres psql -c "%s"' % command.format(**VARS))
    


def locale():
    """ Set locale to enviroment """
    fabric.contrib.files.upload_template(
        'environment.j2', '/etc/environment',
        context=VARS, use_jinja=True, backup=False, use_sudo=True, template_dir=VARS['templates_dir'])
    sudo('localedef {locale}.{encoding} -i {locale} -f{encoding}'.format(**VARS))
    # sudo('locale-gen')


def apt_packages():
    """ Install common packages """
    sudo('apt-get -y update')
    sudo('apt-get -y install libcurl4-gnutls-dev libexpat1-dev gettext libz-dev libssl-dev git redis-server')


@sentinel('python')
def python_packages():
    """ Install python components """

    sudo(
        'apt-get -y install python-dev python-pip python-virtualenv build-essential '
        'libncurses5-dev libncursesw5-dev libreadline6-dev libgdbm-dev libsqlite3-dev '
        'libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libxml2-dev libxslt1-dev')

    with cd('/tmp'):
        # download python source code
        run('wget -O python.tgz https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tgz')
        # extract python tarball
        run('tar -xf python.tgz')
        run('mv Python-3.5.1 python')

    with cd('/tmp/python'):
        # configuring python 3.4 Makefile
        run('./configure --prefix=/usr/local/python-3.5.1')
        # compiling the python 3.4 source code and install
        sudo('make && make altinstall #')
    sudo('rm /tmp/* -rf')
    # make link to python
    sudo('ln -sf /usr/local/python-3.5.1/bin/* /usr/local/bin/')


def app():
    """ Run application tasks """
    with cd(VARS['root_dir']):
        # Create venv and install requirements
        run('pyvenv-3.5 {venv_path}'.format(**VARS))
        
        # Install required python packages with pip from wheels archive
        run('make wheel_install')
        # if running on CI - exit
        if 'CI_FLAG' in os.environ:
            return
        
        # run app tasks for devserver start
        # Copy settings local
        run('cd {project_name} && cp settings_local.py.example settings_local.py'.format(**VARS))
        # collect static files
        for command in ('migrate --noinput', 'collectstatic --noinput', ):  # 'compilemessages', ):
            run('{venv_path}/bin/python manage.py {command}'.format(command=command, **VARS))
        # make root dir available to read
        # sudo('chmod 755 {base_dir}/static -R'.format(**VARS))
        # Create user
        create_user_py = (
            'from django.contrib.auth.models import User'   '\n'
            'User.objects.create_superuser(**{user_data})'  '\n'
        ).format(**VARS)

        run('echo "{create_user_py}" | {venv_path}/bin/python manage.py shell'.format(
            create_user_py=create_user_py, **VARS))
        run('mkdir var -p')

        # Start celery and runserver
        run('make start', pty=False)
        run('make runcelery_multi', pty=False)


    with open('{project_name}/__init__.py'.format(**VARS), 'w') as init_file:
        init_file.write('''# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app  # noqa
''')

