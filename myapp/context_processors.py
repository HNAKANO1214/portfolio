import os


def environment_variables(request):
    return {
        'SITE_TITLE': os.getenv('SITE_TITLE', ''),    # サイトのタイトル
    }
