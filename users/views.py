from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomSignUpForm
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