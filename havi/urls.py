# coding=utf-8
"""havi URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from havi import views
from havi.handler.mission import load_meta, submit, list, show_log

urlpatterns = [
    url('^admin/', admin.site.urls),
    url('^view/', views.index, name="view"),

    url('^submit/', submit.process),
    url('^load-meta/', load_meta.process),
    url('^list/', list.process),
    url('^show-log/', show_log.process),

]
