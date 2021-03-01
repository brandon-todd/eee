from django.db import models
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    email = models.EmailField(max_length = 100, blank = False)
    first_name = models.CharField(max_length = 50, blank = False)
    last_name = models.CharField(max_length = 50, blank= False)
    phone_number = models.CharField(max_length = 13, blank = True)