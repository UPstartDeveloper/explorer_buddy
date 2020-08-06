"""explorer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings

from notes import views


urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('notes/', include('notes.urls')),  # Notes app
    path('api/', include('api.urls')),  # DRF plugin
    path('auth/', include('django.contrib.auth.urls')),  # Built-in auth app
    path('', views.show_landing_page, name="landing_page"),  # landing page
    path('accounts/', include('accounts.urls')),  # User Accounts and User info
]

# used to serve static files in development
if settings.DEBUG is True:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
