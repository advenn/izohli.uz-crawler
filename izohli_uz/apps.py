from django.apps import AppConfig

from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc

from izohli_uz.parser.word_pages import parse_izohli_uz

executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
scheduler = BackgroundScheduler(executors=executors, timezone=utc)
scheduler.add_job(parse_izohli_uz, 'interval', days=1)
scheduler.start()


class IzohliUzConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "izohli_uz"
