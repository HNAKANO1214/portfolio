from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('about/', views.AboutView.as_view(), name='about'),
    # TODO: Pending
    # path('contact/', views.ContactView.as_view(), name='contact'),
]
