﻿# rick-and-morty

start celery worker: celery -A rick_and_morty_api worker --loglevel=INFO --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo

start celery beat: celery -A rick_and_morty_api beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
