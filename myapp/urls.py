from django.views.decorators.cache import cache_page
from django.urls import path

from myapp.views import TopPageView
from myapp.views import DetailView
from myapp.views import AboutView
from myapp.views import DummyRequestView
# from myapp.views import ContactView

app_name = "myapp"
urlpatterns = [
    path('', TopPageView.as_view(), name='top_page'),
    path('detail/<int:pk>', cache_page(60 * 15)(DetailView.as_view()), name='detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('dummy_request/', DummyRequestView.as_view(), name='dummy_request'),
    # TODO: Pending
    # path('contact/', ContactView.as_view(), name='contact'),
]
