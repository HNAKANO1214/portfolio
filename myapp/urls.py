from django.urls import path

from myapp.views import TopPageView
from myapp.views import DetailView
from myapp.views import AboutView
# from myapp.views import ContactView

urlpatterns = [
    path('', TopPageView.TopPageView.as_view(), name='top_page'),
    path('detail/<int:pk>', DetailView.DetailView.as_view(), name='detail'),
    path('about/', AboutView.AboutView.as_view(), name='about'),
    # TODO: Pending
    # path('contact/', ContactView.ContactView.as_view(), name='contact'),
]
