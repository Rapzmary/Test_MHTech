from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics
import json

from Test_MH import manage_user
from django.http import HttpResponse
class registerViewset(generics.ListAPIView):
    queryset = register.objects.all()
    serializer_class = registerSerializer
    def post(self, request, *args, **kwargs):
        message = manage_user.register(request.data)
            
        return HttpResponse(json.dumps({'message':message }), status=200)




class LoginViewset(generics.ListAPIView):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):
        message = manage_user.Login(request.data)
        return HttpResponse(json.dumps({'message':message }), status=200)
        

class Logout(generics.ListAPIView):
    queryset = Logout.objects.all()
    serializer_class = LogoutSerializer
    def post(self, request, *args, **kwargs):
        message = manage_user.Logout(request.data['Token'])
        return HttpResponse(json.dumps({'message':message }), status=200)