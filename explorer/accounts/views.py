from django.shortcuts import render
from accounts.forms import ExplorerSignUpForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

# Create your views here.


def signup(request):
    '''Display form where user can create a new account.'''
    if request.method == 'POST':
        form = ExplorerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = ExplorerSignUpForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
