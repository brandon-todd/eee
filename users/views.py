from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomSignUpForm
from.models import CustomUser
from django.contrib.auth.decorators import login_required
import requests
import smtplib
import os
import string
from smtplib import SMTPServerDisconnected,SMTPConnectError,SMTPHeloError,SMTPAuthenticationError,SMTPSenderRefused,SMTPRecipientsRefused
def index(request):
    return render(request, 'users/index.html')

def logout_view(request):
    """Log the user out."""
    logout(request)
    return render(request, 'users/index.html')

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.   
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # Log the user in, and then redirect to home page.
            authenticated_user = authenticate(username=new_user.username,
                password=request.POST['password1'])
            login(request, authenticated_user)
            return render(request,'users/index.html')

    context = {'form': form}
    return render(request, 'users/register.html', context)
def SignUpView(request):
    try:
        if request.method == 'POST':
            form = CustomSignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.save()
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=user.username,password=raw_password)
                login(request,user)
                return redirect('users:index')
        else:
            form= CustomSignUpForm()
    except:
        raise KeyError
        raise NameError
    return render(request, 'registration/signup.html',{'form':form})
def compare(a,b):
    return [c for c in a if c.isalpha()] == [c for c in b if c.isalpha()]
@login_required(login_url = 'login')
def activate(request):
    sender_address=''
    sender_password =''
    with open('users'+os.sep+'Activate.txt')as f:
        body = f.read()
    numbers = CustomUser.objects.all()
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.ehlo_or_helo_if_needed()
        server.login(sender_address,sender_password)
        for num in numbers:
            if len(num.phone_number)>6:
                if num.service_provider == 'tmobile':
                    phone = str(num.phone_number)+'@tmomail.net'
                elif num.service_provider=='verizon':
                    phone = str(num.phone_number)+'@vtext.com'
                elif num.service_provider =='att':
                    phone = str(num.phone_number)+'@txt.att.net'
                elif num.service_provider == 'sprint':
                    phone = str(num.phone_number)+'@messaging.sprintpcs.com'
                else:
                    print('no service provider')
                    print(num.phone_number)
                    pass
                server.sendmail(sender_address,phone,body)
        server.quit()
    except:
        print("something went wrong")
    return render(request,'registration/activation_text.html')
def scraping(request):
    sites= ['https://twitter.com/inciweb/','https://inciweb.nwcg.gov/','https://twitter.com/wildlandfireaz/lists/wildlandfireaz','https://dffm.az.gov/','https://maps.nwcg.gov/sa/#/%3F/%3F/33.2848/-112.5786/7','https://www.arcgis.com/apps/opsdashboard/index.html#/c0f6fa39f03b4f99b4b345e0d4301c17','https://hub.arcgis.com/search?tags=AZDEMA','https://wildfiresnearme.wfmrda.com/','https://www.yavapai.us/publicworks/emergency-management','https://gacc.nifc.gov/swcc/index.htm','https://gacc.nifc.gov/swcc/predictive/intelligence/daily/SWCC_Morning_Situation_Report/SWCC_Morning_Situation_Report.htm','https://www.wildlandfire.az.gov/wildfire-news','https://gacc.nifc.gov/swcc/dc/azpdc/information/incidents.php','https://www.ycsoaz.gov/community/Emergency-Preparedness/Emergency-Notification-System','https://www.fs.usda.gov/prescott/','https://www.wildfireaz.com/arizona-dispatch-centers/prescott-interagency-dispatch/#','https://www.fs.usda.gov/prescott','https://www.facebook.com/groups/966421680099464','https://www.facebook.com/groups/ArizonaRoadWeatherConditionsReportsUpdates','https://www.facebook.com/groups/478010119643181','https://www.facebook.com/groups/ArizonaEquineEmergency','https://www.facebook.com/groups/459304871350600','https://www.facebook.com/groups/1526217847636057']
@login_required(login_url = 'login')
def RFA_form(request):
    return redirect('https://docs.google.com/forms/d/1EB2ZJCFTAr42_905n4b19XDZn_i2jVQx5jEgqAfW1ws/edit?usp=drive_web')
@login_required(login_url = 'login')
def Check_RFA(request):
    return redirect('https://docs.google.com/spreadsheets/d/11ncAY-75WxHs51cXrdngKvEkFvFvqogE_pjxvXrHB90/edit#gid=36233523')
@login_required(login_url = 'login')
def EEE_Rig(request):
    return redirect('https://docs.google.com/forms/d/19VmZI0E1eR6s77SdnJSeBq8dM26gOIWvaWGtlKkK_44/edit')
@login_required(login_url = 'login')
def Check_Rig(request):
    return redirect('https://docs.google.com/spreadsheets/d/11ncAY-75WxHs51cXrdngKvEkFvFvqogE_pjxvXrHB90/edit#gid=36233523')
@login_required(login_url = 'login')
def Dispatch_Log(request):
    return redirect('https://docs.google.com/forms/d/1n_GP28o48b1gfZ_kV_u-JGiOJbdIn_ugbl2yAqw5NZQ/edit?usp=drive_web')
@login_required(login_url = 'login')
def Check_Dispatch(request):
    return redirect('https://docs.google.com/spreadsheets/d/1_yUSZuWiPl3VfsicMkFMxEgHnJpeqYkUZC8vv4tnwRE/edit#gid=102245832')
@login_required(login_url = 'login')
def Horse_Manager(request):
    return redirect('https://docs.google.com/forms/d/1aw8iBi9MgWKXXqEqH3o3qgSylWIVxUTSSdBpDuRZi_8/edit')
@login_required(login_url = 'login')
def Check_Horse(request):
    return redirect('https://docs.google.com/spreadsheets/d/1DLh0GgrV9wh34mVq9VZLxiR5NxxgykcpMdt3vML02zA/edit#gid=1255265220')