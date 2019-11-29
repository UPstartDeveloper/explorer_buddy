from django.test import TestCase
from accounts.views import signup, PasswordResetView
from django.contrib.auth.models import User, AnonymousUser
from django.test.client import RequestFactory
from django.core import mail
from django.urls import reverse, reverse_lazy


class SignUpViewTests(TestCase):
    '''A new visitor to the site is able to create an account.'''
    def setUp(self):
        '''Instantiate RequestFactory and AnonymousUser to implement tests.'''
        self.factory = RequestFactory()
        self.unknown_user = AnonymousUser()

    def test_account_creation_after_signup(self):
        '''The user creates a new account with a username and password.'''
        # the anonymous user can visit the signup page
        get_request = self.factory.get('accounts:signup-form')
        get_request.user = self.unknown_user
        response = signup(get_request)
        # test that the form looks correct
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sign Up')

        # simulate user making a new account with a username and password
        form_data = {
            'email': 'zain_14@icloud.com',
            'username': 'LittleEinstein',
            'password1': 'Sc1ence_R0cks!',
            'password2': 'Sc1ence_R0cks!'
        }

        post_request = self.factory.post('accounts/signup/', form_data)
        post_request.user = self.unknown_user
        response = signup(post_request)
        # test the view and the User accounts after form submission
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(username=form_data['username'])
        self.assertNotEqual(user, None)
        self.assertEqual(user.email, form_data['email'])


class PasswordResetViewTests(TestCase):
    def setUp(self):
        ''''Instantiate RequestFactory and AnonymousUser to implement tests.'''
        self.factory = RequestFactory()
        self.unknown_user = AnonymousUser()
        self.user = User.objects.create(username='Zain',
                                        email='zain_14@icloud.com',
                                        password='who_is_typing_this_7')
        self.password_reset_url = reverse('accounts:password_reset')

    def test_user_submits_valid_email_to_reset_password(self):
        '''A user who enters an email address
           (already on record in the database) receives a reset email.
        '''
        get_request = self.factory.get(self.password_reset_url)
        response = PasswordResetView.as_view()(get_request)
        # user is able to see the form
        self.assertEqual(response.status_code, 200)

        # user receives an email if the address they submit is in database
        form_data = {
            'email': self.user.email
        }
        user_with_email = User.objects.get(email=self.user.email)
        self.assertTrue(user_with_email, not None)
        response = self.client.post(self.password_reset_url, form_data)
        # user is redirected after submission
        self.assertEqual(response.status_code, 302)
        # an email is sent to the user
        self.assertEqual(len(mail.outbox), 1)
