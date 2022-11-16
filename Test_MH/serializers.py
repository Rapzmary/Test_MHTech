from rest_framework import serializers
from .models import *


class registerSerializer(serializers.ModelSerializer):

    class Meta:
        model = register
        fields = ('firstname', 'lastname', 'date_of_birth', 'email', 'password')

class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Login
        fields = ('email', 'password')
class LogoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logout
        fields = ('Token')

class suggest_bookSerializer(serializers.ModelSerializer):
    class Meta:
        model = suggest_book
        fields = ('Authorization','seat')

