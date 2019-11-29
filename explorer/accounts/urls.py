from django.contrib import admin
from django.urls import path, include
from accounts.views import signup
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from accounts.views import PasswordResetConfirm, PasswordResetView


app_name = 'accounts'
urlpatterns = [
    path('signup/', signup, name='signup-form'),
    path('',
         auth_views.LoginView.as_view(template_name="accounts/login.html"),
         name='login'),
    # views for resetting the password
    path('password-reset/',
         PasswordResetView.as_view(
          template_name='accounts/password_reset/enter_email.html'),
         name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
          template_name='accounts/password_reset/email_sent.html'),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirm.as_view(), name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
                    template_name='accounts/password_reset/complete.html'),
         name='password_reset_complete'),
]
