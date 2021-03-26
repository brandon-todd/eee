from django.urls import path,include
from . import views
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
app_name = 'users'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', LoginView.as_view(template_name='login.html'),name='login'),
    path('dispatch/', views.Dispatch_Log, name='dispatch_log'),
    path('check_dispatch/',views.Check_Dispatch,name ='check_dispatch'),
    path('horse/', views.Horse_Manager, name = 'horse_manager'),
    path('check_horse/',views.Check_Horse, name = 'check_horse'),
    path('RFA/',views.RFA_Form, name= 'rfa_form'),
    path('check_rfa/',views.Check_RFA, name = 'check_rfa'),
    path('trailer/',views.Trailer_Form, name = 'rig_info'),
    path('check_trailer/',views.Check_Trailer,name = 'check_rig'),
    path('signup/', views.SignUp, name = 'signup'),
    path('logout/',views.logout_view, name = 'logout'),
    path('activation/',views.Activate, name = 'activation_text')
]