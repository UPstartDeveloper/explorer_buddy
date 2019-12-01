from django.shortcuts import render
from accounts.forms import ExplorerSignUpForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
import django.contrib.auth.views as auth_views
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.


def signup(request):
    '''Display form where user can create a new account.'''
    if request.method == 'POST':
        form = ExplorerSignUpForm(request.POST)
        if form.is_valid():
            print('the form is valid')
            form.save()
            return redirect(reverse('accounts:login'))
        print('the form is invalid')
    else:
        form = ExplorerSignUpForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)


class PasswordResetView(auth_views.PasswordResetView):
    '''Emails user with a link to reset their password.'''
    success_url = reverse_lazy('accounts:password_reset_done')
    template_name = 'accounts/password_reset/enter_email.html'


class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    '''Presents the form for entering a new password.'''
    success_url = reverse_lazy('accounts:password_reset_complete')
    template_name = 'accounts/password_reset/new_password.html'
