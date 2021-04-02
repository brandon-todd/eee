from rest_framework import serializers
from .models import Active_User
class Active_User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Active_User
        fields = ('available','user','id')
