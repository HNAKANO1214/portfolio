import os

from django.conf import settings


def environment_variables(request):
    return {
        'SITE_TITLE': settings.SITE_TITLE,    # サイトのタイトル
    }
