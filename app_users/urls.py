from django.urls import path

from .views import RegisterView, confirm_email, LoginFormView, AccountUpdateView, PasswordUpdateView

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('account/', AccountUpdateView.as_view(), name='account'),
    path('update/password/', PasswordUpdateView.as_view(), name='update-password'),
    path('verification/<int:uid>/<str:token>', confirm_email, name='confirm-email')
]
