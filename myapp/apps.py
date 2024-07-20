from apscheduler.schedulers.background import BackgroundScheduler
from django.apps import AppConfig

from tasks import dummy_request


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        import myapp.signals        # noqa: F401
        super().ready()

        # Render休眠対策 10分に1回ダミーリクエストを送信
        scheduler = BackgroundScheduler()
        scheduler.add_job(dummy_request, 'interval', minutes=10)
        scheduler.start()
