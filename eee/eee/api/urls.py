from django.urls import path
from . import views
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib import admin
from rest_framework import routers
from django.conf.urls import include
from .views import Active_User_ViewSet

router = routers.DefaultRouter()
router.register('active_user',Active_User_ViewSet)


app_name = 'api'
urlpatterns = [
    path('',include(router.urls)),
]