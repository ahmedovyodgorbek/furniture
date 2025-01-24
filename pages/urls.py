from django import urls
from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('contact/', views.ContactCreateView.as_view(), name='contact'),
    path('about/', views.AboutTemplateView.as_view(), name='about'),
    path('', views.HomeTemplateView.as_view(), name='home'),
]
