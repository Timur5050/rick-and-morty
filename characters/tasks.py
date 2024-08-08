from characters.scraper import sync_characters

from celery import shared_task


@shared_task
def run_sync_with_api():
    return sync_characters()
