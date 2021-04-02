from django.db import models
from users.models import CustomUser
# Create your models here.
class Active_User(models.Model):
    available = models.BooleanField(null = True,blank = True)
    user = models.ForeignKey(CustomUser,default = '', on_delete=models.CASCADE)
    
    def num_available(self):
        av = CustomUser.objects.filter(is_available = True)
        avail = Active_User.object.filer(available = True)
        return av,avail
    class Meta:
        unique_together = (('user','available'),)
        index_together = (('user','available'),)
