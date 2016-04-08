VENV_PATH := /home/vagrant/venv/bin

runserver:
	$(VENV_PATH)/python manage.py runserver 0.0.0.0:8000

start:
	$(VENV_PATH)/gunicorn --preload -D -b 127.0.0.1:8000 falstartexample.wsgi:application

pep8:
	$(VENV_PATH)/pep8 --exclude=*migrations*,*settings_local.py* --max-line-length=119 --show-source  falstartexample/

pyflakes:
	$(VENV_PATH)/pylama --skip=*migrations* -l pyflakes falstartexample/

lint:
	make pep8
	make pyflakes

test:
	$(VENV_PATH)/python manage.py test falstartexample -v 2 --noinput

ci_test:
	make test
	make lint

wheel_install:
	$(VENV_PATH)/pip install --no-index -f wheels/ -r requirements.txt

runcelery:
	$(VENV_PATH)/celery -A falstartexample worker -l info -B -s ./var/celerybeat-schedule

runcelery_multi:
	$(VENV_PATH)/celery multi restart falstartexample_worker \
		-A falstartexample -l info -B -s ./var/celerybeat-schedule \
			--logfile="./var/celery_%n.log" \
				--pidfile="./var/celery_%n.pid"

