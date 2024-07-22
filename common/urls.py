from django.urls import path
from .views import set_language

app_name = "common"
urlpatterns = [
    path('set_language/<str:lang_code>/', set_language, name='set_language'),
]
