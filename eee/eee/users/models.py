from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(max_length = 50,name ='email')
    first_name = models.CharField(max_length = 50, blank = False)
    last_name = models.CharField(max_length = 50,blank = False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17,name = 'phone_number')
    is_available = models.BooleanField(blank = True,null = True)
    class Meta:
        managed = True
        db_table = 'users'