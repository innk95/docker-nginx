
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from my_app import views


urlpatterns = [
    url(r'^authorization', views.Authorization.as_view()),
    url(r'^registration', views.Registration.as_view()),
    url(r'^logout', views.Logout.as_view()),
    url(r'^profile$', views.Profile.as_view()),
]
