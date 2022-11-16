from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics
import json

from Test_MH import manageText
from django.http import HttpResponse
class registerViewset(generics.ListAPIView):
    queryset = register.objects.all()
    serializer_class = registerSerializer
    def post(self, request, *args, **kwargs):
        first_name = request.data['firstname']
        last_name = request.data['lastname']
        date_of_birth =request.data['date_of_birth']
        email = request.data['email']
        password = request.data['password']
        with open("Data_user.txt") as f:
            lines = f.readlines()
        message = ""
        diplicate = False
        for i in lines:
            if i == email:
                diplicate = True
                return HttpResponse(json.dumps({'message':"Email ซ้ำ" }), status=200)
        if diplicate is False:
            f = open('C:/Users/suwan/employees.txt', 'a')
            
            return HttpResponse(json.dumps({'message':"Regiter success" }), status=200)




class LoginViewset(generics.ListAPIView):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):
        email = request.data['email']
        password = request.data['password']

class Logout(generics.ListAPIView):
    queryset = Logout.objects.all()
    serializer_class = LogoutSerializer