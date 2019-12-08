from django.shortcuts import render
from accounts.forms import ExplorerSignUpForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
import django.contrib.auth.views as auth_views
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from accounts.models import Profile


class SignUpView(CreateView):
    '''Display form where user can create a new account.'''
    form_class = ExplorerSignUpForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        '''Save the new User, and a new Profile for them, in the database.'''
        self.object = form.save()
        Profile.objects.create(user=self.object)
        return super().form_valid(form)


class PasswordResetView(auth_views.PasswordResetView):
    '''Emails user with a link to reset their password.'''
    success_url = reverse_lazy('accounts:password_reset_done')
    template_name = 'accounts/password_reset/enter_email.html'
    email_template_name = 'accounts/password_reset/email_to_user.html'


class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    '''Presents the form for entering a new password.'''
    success_url = reverse_lazy('accounts:password_reset_complete')
    template_name = 'accounts/password_reset/new_password.html'
