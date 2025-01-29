import threading

from django.contrib.auth import get_user_model, login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView

from .forms import RegisterForm, LoginForm, AccountFrom
from .utils import send_email_confirmation

UserMdel = get_user_model()


class LoginFormView(FormView):
    template_name = 'auth/user-login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        login(request=self.request, user=form.cleaned_data['user'])
        messages.success(self.request, 'Success !')

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Something went wrong! ')
        return super().form_invalid(form)


class RegisterView(FormView):
    template_name = 'auth/user-register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        email_thread = threading.Thread(target=send_email_confirmation, args=(user, self.request,))
        email_thread.start()

        messages.success(self.request, 'Please confirm your email !')

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Something went wrong! ')
        return super().form_invalid(form)


def confirm_email(request, uid, token):
    try:
        user = UserMdel.objects.get(id=uid)
    except UserMdel.DoesNotExist:
        return redirect('/')

    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your email address has been verified')
        return redirect('/')
    else:
        messages.error(request, 'Link is not correct')
        return redirect('/')


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'auth/user-account.html'
    form_class = AccountFrom
    success_url = reverse_lazy('users:account')
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user


class PasswordUpdateView(FormView):
    template_name = 'auth/update-password.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('users:update-password')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        data = form.cleaned_data
        user = self.request.user
        user.set_password(raw_password=data['new_password1'])
        messages.success(self.request, 'Your password has been changed successfully! ')
        user.save()

        update_session_auth_hash(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Password is invalid, Try again')
        return super().form_invalid(form)
