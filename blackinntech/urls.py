"""blackinntech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login
from blackinntech import  views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [
    url(r'^admin/', admin.site.urls, name = 'admin'),
    url(r'^crm/', include('crm.urls', namespace='crm')),
    url(r'^$', views.index, name='index'),
    url(r'^accounts/login/', login, {'template_name':'login.html'}, name='login'),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^logged/$', views.logged_in , name ="logged_in"),
]

urlpatterns += staticfiles_urlpatterns()
