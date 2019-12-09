from django.shortcuts import render
from accounts.forms import ExplorerSignUpForm
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
import django.contrib.auth.views as auth_views
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from accounts.models import Profile
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class SignUpView(SuccessMessageMixin, CreateView):
    '''Display form where user can create a new account.'''
    form_class = ExplorerSignUpForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'
    success_message = 'Welcome to Explorer Buddy! You may now log in.'

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


class ProfileDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile/view.html'
    login_url = 'accounts:login'
    queryset = User.objects.all()

    def get(self, request, pk):
        """Renders a page to show a specific note in full detail.
           Parameters:
           user_id(int): pk of the User object requesting the page
           request(HttpRequest): the HTTP request sent to the server

           Returns:
           render: a page of the Profile information

        """
        user = self.queryset.get(id=pk)
        profile = user.profile
        context = {
            'profile': profile
        }
        return render(request, self.template_name, context)

    def test_func(self):
        '''Ensures that users can only view their own Profiles.'''
        user = self.get_object()
        return (self.request.user.profile == user.profile)


class ProfileUpdate(UpdateView):
    template_name = 'accounts/profile/edit.html'


class ProfileDelete(DeleteView):
    template_name = 'accounts/profile/delete.html'
