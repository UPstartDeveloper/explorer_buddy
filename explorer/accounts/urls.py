from django.contrib import admin
from django.urls import path, include
from accounts.views import signup
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


app_name = 'accounts'
urlpatterns = [
    path('signup/', signup, name='signup-form'),
]
