from django.contrib import admin
from django.urls import path, include
from accounts.views import SignUpView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = 'accounts'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup-form'),
]
