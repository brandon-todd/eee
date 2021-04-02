from django.shortcuts import render,redirect 
from django.contrib.auth import login,logout,authenticate
from .forms import CustomUserCreationForm, Active
from django.contrib.auth.decorators import login_required
from .models import CustomUser
# Create your views here.

def index(request):
    return render(request, 'index.html')
@login_required
def Dispatch_Log(request):
    return redirect('https://docs.google.com/forms/d/1n_GP28o48b1gfZ_kV_u-JGiOJbdIn_ugbl2yAqw5NZQ/edit?usp=drive_web')
@login_required
def Check_Dispatch(request):
    return redirect('https://docs.google.com/spreadsheets/d/1_yUSZuWiPl3VfsicMkFMxEgHnJpeqYkUZC8vv4tnwRE/edit#gid=102245832')
@login_required
def Horse_Manager(request):
    return redirect('https://docs.google.com/forms/d/1aw8iBi9MgWKXXqEqH3o3qgSylWIVxUTSSdBpDuRZi_8/edit')
@login_required
def Check_Horse(request):
    return redirect('https://docs.google.com/spreadsheets/d/1DLh0GgrV9wh34mVq9VZLxiR5NxxgykcpMdt3vML02zA/edit#gid=1255265220')
@login_required
def RFA_Form(request):
    return redirect('https://docs.google.com/forms/d/1EB2ZJCFTAr42_905n4b19XDZn_i2jVQx5jEgqAfW1ws/edit')
@login_required
def Check_RFA(request):
    return redirect('https://docs.google.com/spreadsheets/d/11ncAY-75WxHs51cXrdngKvEkFvFvqogE_pjxvXrHB90/edit#gid=36233523')
@login_required
def Trailer_Form(request):
    return redirect('https://docs.google.com/forms/d/19VmZI0E1eR6s77SdnJSeBq8dM26gOIWvaWGtlKkK_44/edit')
@login_required
def Check_Trailer(request):
    return redirect('https://docs.google.com/spreadsheets/d/1bDsiVqP9_nAeP2ZPVIH9Gh71JjGfeNy-8yfl0v_9xXI/edit#gid=1043994411')
def SignUp(request):
    if request.method != 'POST':
        form = CustomUserCreationForm
    else:
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,password=request.POST['password1'])
            login(request,authenticated_user)
        return render(request,'index.html')
    context={'form':form}    
    return render(request,'signup.html',context)

def logout_view(request):
    logout(request)
    return redirect('users:index')

@login_required
def Activate(request):
    if request.method != 'POST':
        form = Active
    else:
        form = Active(instance = request.user, data = request.POST)
        if form.is_valid():
            form.save()
        return render(request,'active.html')
    context = {'form':form}
    return render(request, 'active.html',context)