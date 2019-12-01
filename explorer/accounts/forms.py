from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

# credit for subclassing forms.Form belongs to
# https://overiq.com/django-1-10/django-creating-users-using-usercreationform/


class ExplorerSignUpForm(UserCreationForm):
    '''A form that handles registering new users.'''
    # email = forms.EmailField(required=True,
                             # help_text="Must include the '@' symbol.")

    class Meta:
        model = User
        fields = ['email', 'username',
                  'first_name', 'last_name',
                  'password1', 'password2']

    def save(self, commit=True):
        '''Initializes fields of the new User instance.'''
        user = super(ExplorerSignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit is True:
            user.save()

        return user


"""
class ExplorerSignUpForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=3,
                               max_length=150)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password',
                                widget=forms.PasswordInput)

    def clean_username(self):
        '''Validate if the user input is an acceptable username.'''
        username = self.cleaned_data['username']
        # make sure there is not already a user with this username
        same_username = User.objects.filter(username=username)
        if same_username.count() is not 0:
            raise ValidationError("Username already exists")
        else:
            return username

    def clean_email(self):
        '''Make sure that there is not already another User with is email.'''
"""
