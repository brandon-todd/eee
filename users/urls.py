from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import SignUpView, logout_view
app_name = 'users'

urlpatterns = [
    path('home', views.index, name='index'),
        
    # Logout page.
    path('logout/', views.logout_view, name='logout'),
    
    # Registration page. 
    path('signup/', views.SignUpView, name='signup'),
]