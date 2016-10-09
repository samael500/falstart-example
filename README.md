# falstart-example
Example of the [falstart](https://github.com/Samael500/falstart)-utility result to create a basic project in Django

![falstart example](example.gif)

```Shell
$ falstart falstart-example
> Django version ['1.9.5'] 1.10.2
> Debian version (for vagrant box) ['jessie64']
> Python version ['3.5.1'] 3.5.2
> Vagrant box IP-addr ['10.1.1.123'] 10.1.1.111
> Do you nead a POSTGRES? [Y/n]
> Do you nead a CELERY? [y/N] y
> Do you nead a REDIS? [y/N] y
> Do you nead a SENTRY? [y/N] y
> Database name ['falstartexample_db']
> Database user ['falstartexample_user']
> Database pass ['VJJxu87Ki']
[falstart] > make dir: "/home/maks/temp/falstart-example"
[falstart] > render "Vagrantfile.j2" > "Vagrantfile"
[falstart] > render "Makefile.j2" > "Makefile"
[falstart] > run: "chmod +x Makefile"
[falstart] > make dir: "provision"
[falstart] > make dir: "provision"
[falstart] > render "provision_fabfile.j2" > "provision/fabric_provisioner.py"
[falstart] > render "requirements.j2" > "requirements.txt"
[falstart] > render "requirements.j2" > "requirements-remote.txt"
[falstart] > render "lintrc.j2" > ".lintrc"
[falstart] > render "coveragerc.j2" > ".coveragerc"
[falstart] > make dir: "falstartexample"
[falstart] > render "py_codes/settings_local.j2" > "falstartexample/settings_local.py.example"
[falstart] > make dir: "falstartexample"
[falstart] > render "py_codes/celery.j2" > "falstartexample/celery.py"
[falstart] > copy: "/home/maks/s50/falstart/falstart/templates/vagrant_templates" > "provision/templates"
[falstart] > run: "vagrant up"
Bringing machine 'falstartexample_vagrant' up with 'virtualbox' provider...
==> falstartexample_vagrant: Checking if box 'debian/jessie64' is up to date...
==> falstartexample_vagrant: A newer version of the box 'debian/jessie64' is available! You currently
==> falstartexample_vagrant: have version '8.4.0'. The latest is version '8.6.1'. Run
==> falstartexample_vagrant: `vagrant box update` to update.
==> falstartexample_vagrant: Clearing any previously set forwarded ports...
==> falstartexample_vagrant: Fixed port collision for 22 => 2222. Now on port 2200.
==> falstartexample_vagrant: Clearing any previously set network interfaces...
==> falstartexample_vagrant: Preparing network interfaces based on configuration...
    falstartexample_vagrant: Adapter 1: nat
    falstartexample_vagrant: Adapter 2: hostonly
==> falstartexample_vagrant: Forwarding ports...
    falstartexample_vagrant: 22 (guest) => 2200 (host) (adapter 1)
==> falstartexample_vagrant: Running 'pre-boot' VM customizations...
==> falstartexample_vagrant: Booting VM...
==> falstartexample_vagrant: Waiting for machine to boot. This may take a few minutes...
    falstartexample_vagrant: SSH address: 127.0.0.1:2200
    falstartexample_vagrant: SSH username: vagrant
    falstartexample_vagrant: SSH auth method: private key
==> falstartexample_vagrant: Machine booted and ready!
==> falstartexample_vagrant: Checking for guest additions in VM...
    falstartexample_vagrant: No guest additions were detected on the base box for this VM! Guest
    falstartexample_vagrant: additions are required for forwarded ports, shared folders, host only
    falstartexample_vagrant: networking, and more. If SSH fails on this machine, please install
    falstartexample_vagrant: the guest additions and repackage the box to continue.
    falstartexample_vagrant:
    falstartexample_vagrant: This is not an error message; everything may continue to work properly,
    falstartexample_vagrant: in which case you may ignore this message.
==> falstartexample_vagrant: Setting hostname...
==> falstartexample_vagrant: Configuring and enabling network interfaces...
==> falstartexample_vagrant: Exporting NFS shared folders...
==> falstartexample_vagrant: Preparing to edit /etc/exports. Administrator privileges will be required...
[sudo] пароль для maks:
● nfs-server.service - NFS server and services
   Loaded: loaded (/lib/systemd/system/nfs-server.service; enabled; vendor preset: enabled)
   Active: active (exited) since Вс 2016-10-09 14:40:14 MSK; 4min 16s ago
  Process: 1081 ExecStart=/usr/sbin/rpc.nfsd $RPCNFSDARGS (code=exited, status=0/SUCCESS)
  Process: 1073 ExecStartPre=/usr/sbin/exportfs -r (code=exited, status=0/SUCCESS)
 Main PID: 1081 (code=exited, status=0/SUCCESS)
   CGroup: /system.slice/nfs-server.service

окт 09 14:40:13 zlm systemd[1]: Starting NFS server and services...
окт 09 14:40:14 zlm systemd[1]: Started NFS server and services.
==> falstartexample_vagrant: Mounting NFS shared folders...
==> falstartexample_vagrant: Running provisioner: fabric...
[127.0.0.1] Executing task 'common'
[127.0.0.1] put: <file obj> -> /etc/environment
[127.0.0.1] sudo: localedef ru_RU.UTF-8 -i ru_RU -fUTF-8
[127.0.0.1] sudo: touch /usr/locale_8913242974480500368
[127.0.0.1] sudo: apt-get -y update
[127.0.0.1] sudo: apt-get -y install libcurl4-gnutls-dev libexpat1-dev gettext libz-dev libssl-dev git redis-server
[127.0.0.1] sudo: touch /usr/apt_packages_-3330926058430280198
[127.0.0.1] sudo: apt-get -y install python-dev python-pip python-virtualenv build-essential libncurses5-dev libncursesw5-dev libreadline6-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libxml2-dev libxslt1-dev
[127.0.0.1] run: wget -O python.tgz https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz
[127.0.0.1] run: tar -xf python.tgz
[127.0.0.1] run: mv Python-3.5.2 python
[127.0.0.1] run: ./configure --prefix=/usr/local/python-3.5.2
[127.0.0.1] run: make
[127.0.0.1] sudo: make altinstall
[127.0.0.1] sudo: rm /tmp/* -rf
[127.0.0.1] sudo: ln -sf /usr/local/python-3.5.2/bin/* /usr/local/bin/
[127.0.0.1] sudo: touch /usr/python_packages_-535002765752534493
[127.0.0.1] Executing task 'database'
[127.0.0.1] sudo: apt-get -y install postgresql postgresql-server-dev-all python-psycopg2
[127.0.0.1] run: sudo -u postgres psql -c "CREATE USER falstartexample_user;"
[127.0.0.1] run: sudo -u postgres psql -c "ALTER USER falstartexample_user WITH PASSWORD 'VJJxu87Ki';"
[127.0.0.1] run: sudo -u postgres psql -c "ALTER USER falstartexample_user CREATEDB;"
[127.0.0.1] run: sudo -u postgres psql -c "CREATE DATABASE falstartexample;"
[127.0.0.1] run: sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE falstartexample TO falstartexample_user;"
[127.0.0.1] sudo: touch /usr/database_-8337542331712744645
[127.0.0.1] Executing task 'nginx'
[127.0.0.1] sudo: apt-get -y install nginx
[127.0.0.1] sudo: touch /usr/nginx_install_1687306290436383039
[127.0.0.1] put: <file obj> -> /etc/nginx/sites-available/falstartexample
[127.0.0.1] sudo: ln -sf /etc/nginx/sites-available/falstartexample /etc/nginx/sites-enabled/falstartexample
[127.0.0.1] sudo: service nginx restart
[127.0.0.1] Executing task 'app'
[127.0.0.1] run: pyvenv-3.5 /home/vagrant/venv
[127.0.0.1] run: /home/vagrant/venv/bin/pip install -U pip wheel
[127.0.0.1] run: mkdir -p wheels
[127.0.0.1] run: /home/vagrant/venv/bin/pip wheel -w wheels/ -r requirements-remote.txt --pre
[127.0.0.1] run: make wheel_install
[127.0.0.1] run: /home/vagrant/venv/bin/django-admin startproject falstartexample .
[127.0.0.1] run: cd falstartexample && cp settings_local.py.example settings_local.py
[127.0.0.1] Executing task 'localserver'
[127.0.0.1] run: /home/vagrant/venv/bin/python manage.py migrate --noinput
[127.0.0.1] run: /home/vagrant/venv/bin/python manage.py collectstatic --noinput
[127.0.0.1] run: echo "from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.create_superuser(**{'username': 'root', 'password': '123123', 'email': 'root@e.co'})
" | /home/vagrant/venv/bin/python manage.py shell
[127.0.0.1] run: mkdir var -p
[127.0.0.1] run: make start
[127.0.0.1] run: make runcelery_multi

Done.
Disconnecting from 127.0.0.1:2200... done.

==> falstartexample_vagrant: Machine 'falstartexample_vagrant' has a post `vagrant up` message. This is a message
==> falstartexample_vagrant: from the creator of the Vagrantfile, and not from Vagrant itself:
==> falstartexample_vagrant:
==> falstartexample_vagrant: falstartexample dev server successfuly started.
==> falstartexample_vagrant:     Connect to host with:
==> falstartexample_vagrant:     http://10.1.1.111/
==> falstartexample_vagrant:     or over ssh with `vagrant ssh`
==> falstartexample_vagrant:
==> falstartexample_vagrant:     Admin user credentials:
==> falstartexample_vagrant:       login: root
==> falstartexample_vagrant:       password: 123123
==> falstartexample_vagrant:
[falstart] > make dir: "provision"
[falstart] > render "provision_fabfile.j2" > "provision/fabric_provisioner.py"
[falstart] > render "gitignore.j2" > ".gitignore"
[falstart] > Update .gitignore
[falstart] > run: "git add . && git commit -m ":rocket: falstart init commit""
[master 0b93d53] :rocket: falstart init commit
 39 files changed, 690 insertions(+), 4 deletions(-)
 create mode 100644 .coveragerc
 create mode 100644 .falstart.json
 create mode 100644 .lintrc
 create mode 100755 Makefile
 create mode 100644 Vagrantfile
 create mode 100644 falstartexample/__init__.py
 create mode 100644 falstartexample/celery.py
 create mode 100644 falstartexample/settings.py
 create mode 100644 falstartexample/settings_local.py.example
 create mode 100644 falstartexample/urls.py
 create mode 100644 falstartexample/wsgi.py
 create mode 100755 manage.py
 create mode 100644 provision/fabric_provisioner.py
 create mode 100644 provision/templates/environment.j2
 create mode 100644 provision/templates/locale.gen.j2
 create mode 100644 provision/templates/nginx-host.j2
 create mode 100644 requirements-remote.txt
 create mode 100644 requirements.txt
 create mode 100644 wheels/Django-1.10.2-py2.py3-none-any.whl
 create mode 100644 wheels/amqp-1.4.9-py2.py3-none-any.whl
 create mode 100644 wheels/anyjson-0.3.3-py3-none-any.whl
 create mode 100644 wheels/billiard-3.3.0.23-py3-none-any.whl
 create mode 100644 wheels/celery-3.1.23-py2.py3-none-any.whl
 create mode 100644 wheels/contextlib2-0.5.4-py2.py3-none-any.whl
 create mode 100644 wheels/coverage-4.2-cp35-cp35m-linux_x86_64.whl
 create mode 100644 wheels/coverage_badge-0.1.2-py3-none-any.whl
 create mode 100644 wheels/django_rainbowtests-0.5.1-py3-none-any.whl
 create mode 100644 wheels/gunicorn-19.4.5-py2.py3-none-any.whl
 create mode 100644 wheels/kombu-3.0.37-py2.py3-none-any.whl
 create mode 100644 wheels/mccabe-0.4.0-py2.py3-none-any.whl
 create mode 100644 wheels/pep257-0.7.0-py2.py3-none-any.whl
 create mode 100644 wheels/pep8-1.7.0-py2.py3-none-any.whl
 create mode 100644 wheels/psycopg2-2.6.1-cp35-cp35m-linux_x86_64.whl
 create mode 100644 wheels/pyflakes-1.0.0-py2.py3-none-any.whl
 create mode 100644 wheels/pylama-7.0.7-py2.py3-none-any.whl
 create mode 100644 wheels/pytz-2016.7-py2.py3-none-any.whl
 create mode 100644 wheels/raven-5.26.0-py2.py3-none-any.whl
 create mode 100644 wheels/redis-2.10.5-py2.py3-none-any.whl
```