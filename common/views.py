from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils import translation


def set_language(request, lang_code):
    translation.activate(lang_code)
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
    return response
