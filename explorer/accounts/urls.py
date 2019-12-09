from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from accounts.views import (
    PasswordResetConfirm,
    PasswordResetView,
    SignUpView,
    ProfileDetail,
    ProfileUpdate,
    ProfileDelete)


app_name = 'accounts'
urlpatterns = [
    # paths to signup, login, and logout
    path('signup/', SignUpView.as_view(template_name='accounts/signup.html'),
         name='signup-form'),
    path('',
         auth_views.LoginView.as_view(template_name="accounts/login.html"),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(), name='logout'),
    # views to see/change account info
    path('<int:user_id>/profile/', ProfileDetail.as_view(), name='user_info'),
    # views for resetting the password
    path('password-reset/', PasswordResetView.as_view(),
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
