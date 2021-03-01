from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser

class CustomSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length = 100)
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    phone_number = forms.CharField(max_length = 13)
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name','last_name','email','phone_number')