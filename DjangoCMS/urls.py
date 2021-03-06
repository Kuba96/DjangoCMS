"""DjangoCMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path
from articles.views import articles
from DjangoCMS import views


urlpatterns = [
    path('', articles),
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('accounts/', include('userprofile.urls')),
    path('messages/', include('private_messages.urls')),
    path('accounts/login/', views.login),
    path('accounts/auth/', views.auth_view),
    path('accounts/logout/', views.logout),
    path('accounts/loggedin/', views.loggedin),
    path('accounts/invalid/', views.invalid),
    path('accounts/register/', views.register),
    path('accounts/register_success/', views.register_success),
    path('ajax/', views.ajax),
]
