from django.db import models
from django.contrib.auth.models import AbstractUser
services = [
    ('none','--None--'),
    ('sprint','Sprint'),
    ('verizon','Verizon'),
    ('att','AT&T'),
    ('tmobile','T-Mobile')
]

class CustomUser(AbstractUser):
    email = models.EmailField(max_length = 100, blank = False)
    first_name = models.CharField(max_length = 50, blank = False)
    last_name = models.CharField(max_length = 50, blank= False)
    phone_number = models.CharField(max_length = 13, blank = True)
    service_provider = models.CharField(max_length=20, choices = services,default='none')