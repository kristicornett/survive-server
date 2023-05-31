from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from survive.views import register_user, login_user
from rest_framework import routers