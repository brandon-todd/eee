from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Active_User
from users.models import CustomUser
from .serializers import Active_User_Serializer
# Create your views here.
class Active_User_ViewSet(viewsets.ModelViewSet):
    queryset = Active_User.objects.all()
    serializer_class = Active_User_Serializer

    @action(detail = True, methods= ['POST','PUT'])
    def update_active(self,request,pk=None):
        if 'user' in request.data:
            users = request.user
            av = request.data['available']
            try:
                avail = Active_User.objects.get(user= users.id)
                users.available = True
                users.save()
                serializer = Active_User_Serializer(users,many = False)
            except:
                return redirect('http://localhost:8000/users/signup/')
            response = {'message':'its working','result':'serializer.data'}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message':'login first'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
    @action(detail=True,methods = ['GET'])
    def num_available(self,request,pk=None):
        av = CustomUser.objects.filter(is_available = True)
        avail = Active_User.objects.filter(available = True)
        response = {f'messeage':f'{av}{avail}'}
        return Response(response,status = status.HTTP_200_OK)