from django.conf import settings


def environment_variables(request):
    has_seen_animation = request.COOKIES.get('has_seen_animation')
    return {
        'SITE_TITLE': settings.SITE_TITLE,    # サイトのタイトル
        'COPYRIGHT': settings.COPYRIGHT,      # 著作権表示
        'has_seen_animation': has_seen_animation,
    }
