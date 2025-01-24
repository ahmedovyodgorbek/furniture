from django import urls
from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('<int:pk>/', views.BlogDetailView.as_view(), name='detail'),
    path('', views.BlogsTemplateView.as_view(), name='blog-list')
]
