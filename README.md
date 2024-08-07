# rick-and-morty

# Run program using GitHub
To run Celery with both a worker and beat scheduler in separate terminals, you can follow these instructions. This will ensure your Celery tasks are processed and scheduled correctly. Below is a step-by-step guide for setting up and starting the Celery worker and Celery beat scheduler.
### You need to have docker installed

```sh
# Clone the repository
git clone https://github.com/Timur5050/rick-and-morty.git
# Change to the project directory
cd rick-and-morty
# Create a virtual environment
python -m venv venv
# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
# Install required packages
pip install -r requirements.txt
# Create new Postgres DB & User
# Copy sample.env -> .env and populate with all required data 
# Apply migrations
python manage.py migrate

# Run Redis Server
docker run -d -p 6379:6379 redis

# Terminal 1: Start Celery Worker
- celery -A rick_and_morty_api worker --loglevel=INFO --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo

# Terminal 2: Start Celery Beat Scheduler
- start celery beat in celery beat: celery -A rick_and_morty_api beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

# Create schedule for running sync in DB
run app: python manage.py runserver
```
