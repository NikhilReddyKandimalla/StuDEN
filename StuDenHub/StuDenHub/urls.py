"""StuDenHub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from userapp import views as admins

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', admins.index, name="index"),
    path('home/', admins.Home, name="Home"),
    path('adminlogin/', admins.adminlogin, name="adminlogin"),
    path('adminloginaction/',admins.adminloginaction, name='adminloginaction'),

    path('userlogin/', admins.userlogin, name='userlogin'),
    path('userregisterpage/',admins.userregisterpage, name='userregisterpage'),
    path('userregisterAction/', admins.userregisterAction, name='userregisterAction'),
    path('userloginaction/', admins.userloginaction, name='userloginaction'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
