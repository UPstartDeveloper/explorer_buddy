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
from accounts.forms import ProfileForm
from django.urls import reverse
from django.utils.datastructures import MultiValueDict


class SignUpView(SuccessMessageMixin, CreateView):
    '''Display form where user can create a new account.'''
    form_class = ExplorerSignUpForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'
    success_message = 'Welcome to Explorer Buddy! You may now log in.'

    def form_valid(self, form):
        '''Save the new User, and a new Profile for them, in the database.'''
        self.object = form.save()
        profile = Profile.objects.create(user=self.object)
        profile.save()
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


class PasswordChangeStartView(SuccessMessageMixin,
                              auth_views.PasswordChangeView):
    '''Present a form to enter a new password for the authenticated user.'''
    template_name = 'accounts/password_change/password_change_form.html'
    success_url = reverse_lazy('accounts:password_change_done')
    success_message = 'Your password was changed successfully!'


class PasswordChangeComplete(auth_views.PasswordChangeDoneView):
    template_name = 'accounts/profile/view.html'
    success_message = 'Your password was changed successfully!'


class ProfileDetail(DetailView):
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


class ProfilePictureUpdate(UpdateView):
    template_name = 'accounts/profile/edit_image.html'
    form_class = ProfileForm
    queryset = User.objects.all()

    def get_success_url(self):
        '''Redirect to the profile page of the User.'''
        url = self.object.profile.get_absolute_url()
        return url

    def leave_mugshot_unchanged(self, form):
        '''Leave the mugshot field as its current value.'''
        current_image = form.instance.profile.mugshot
        form.instance.profile.mugshot = current_image

    def form_valid(self, form):
        '''Changes the image of the user's profile.'''
        uploaded_image = self.request.FILES.get('mugshot')
        if uploaded_image is not None:
            form.instance.profile.mugshot = uploaded_image
        else:
            # if the user submits without uploading, then no change
            self.leave_mugshot_unchanged(form)
        form.instance.profile.save()
        return super().form_valid(form)


class UserInfoUpdate(UpdateView):
    template_name = 'accounts/profile/edit_info.html'
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']
    queryset = User.objects.all()

    def get_success_url(self):
        '''Redirect to the profile page of the User.'''
        url = self.object.profile.get_absolute_url()
        return url


class UserDelete(DeleteView):
    model = User
    template_name = 'accounts/profile/delete.html'
    success_url = reverse_lazy('accounts:login')
    queryset = User.objects.all()

    def get(self, request, pk):
        """Renders a page to delete the account of the user.
           Parameters:
           user_id(int): pk of the User object requesting the page
           request(HttpRequest): the HTTP request sent to the server

           Returns:
           render: a page to confirm the delete

        """
        user = self.queryset.get(id=pk)
        profile = user.profile
        context = {
            'profile': profile
        }
        return render(request, self.template_name, context)
