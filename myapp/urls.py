from django.urls import path

from myapp.views import TopPageView
from myapp.views import DetailView
from myapp.views import AboutView
# from myapp.views import ContactView

urlpatterns = [
    path('', TopPageView.as_view(), name='top_page'),
    path('detail/<int:pk>', DetailView.as_view(), name='detail'),
    path('about/', AboutView.as_view(), name='about'),
    # TODO: Pending
    # path('contact/', ContactView.as_view(), name='contact'),
]
