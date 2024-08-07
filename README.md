# rick-and-morty

# run celery scheduled tasks
To run Celery with both a worker and beat scheduler in separate terminals, you can follow these instructions. This will ensure your Celery tasks are processed and scheduled correctly. Below is a step-by-step guide for setting up and starting the Celery worker and Celery beat scheduler.
### Terminal 1: Start Celery Worker
- celery -A rick_and_morty_api worker --loglevel=INFO --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo
### Terminal 2: Start Celery Beat Scheduler
- start celery beat in celery beat: celery -A rick_and_morty_api beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
