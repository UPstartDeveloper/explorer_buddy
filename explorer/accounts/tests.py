from django.test import TestCase, LiveServerTestCase
from accounts.views import SignUpView, PasswordResetView
from django.contrib.auth.models import User, AnonymousUser
from django.test.client import RequestFactory
from django.core import mail
from django.urls import reverse, reverse_lazy
from selenium.webdriver.safari.webdriver import WebDriver
from django.contrib.messages.storage.fallback import FallbackStorage


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
        response = SignUpView.as_view()(get_request)
        # test that the form looks correct
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sign Up')

        # simulate user making a new account with a username and password
        form_data = {
            'email': 'zain_14@icloud.com',
            'username': 'LittleEinstein',
            'first_name': 'Zain',
            'last_name': 'Raza',
            'password1': 'Sc1ence_R0cks!',
            'password2': 'Sc1ence_R0cks!'
        }

        post_request = self.factory.post('/signup/', form_data)
        post_request.user = self.unknown_user
        # supply the message to the request
        setattr(post_request, 'session', 'session')
        messages = FallbackStorage(post_request)
        setattr(post_request, '_messages', messages)
        response = SignUpView.as_view()(post_request)
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

        """
class SideNavbarTests(LiveServerTestCase):
    '''Tests that the side navbar takes the entire height of the viewport.'''
    # fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        '''Instantiate needed tools to run tests. Use Heroku as server.'''
        cls.live_server_url = 'https://explorer-buddy.herokuapp.com'
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        '''Deconstruct tools used during tests.'''
        cls.selenium.quit()
        super().tearDownClass()

    def test_sidebar_on_safari(self):
        '''The login page displays the navbar down the side of the page.'''
        self.selenium.get(f'{self.live_server_url}')
"""
