from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
from . import views
from .views import SignUpView,Check_Horse, logout_view,Check_Dispatch,Horse_Manager, Dispatch_Log, activate,EEE_Rig, RFA_form,Check_RFA,Check_Rig
app_name = 'users'

urlpatterns = [
    path('home', views.index, name='index'),
        
    # Logout page.
    path('logout/', views.logout_view, name='logout'),
    
    # Registration page. 
    path('signup/', views.SignUpView, name='signup'),
    
    # Tasks
    path('activation_text/', views.activate, name='activation_text'),
    path('RFA_form/', views.RFA_form, name = 'rfa_form'),
    path('Check_RFA/',views.Check_RFA,name = 'check_rfa'),
    path('Rig_info/',views.EEE_Rig, name = 'rig_info'),
    path('Check_Rig/',views.Check_Rig,name = 'check_rig'),
    path('Dispatch_Log/',views.Dispatch_Log, name = 'dispatch_log'),
    path('Check_Dispatch/',views.Check_Dispatch, name = 'check_dispatch'),
    path('Horse_Manager/', views.Horse_Manager, name = 'horse_manager'),
    path('Check_Horse_Manager/',views.Check_Horse, name = 'check_horse'),
]