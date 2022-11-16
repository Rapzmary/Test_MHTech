from django.db import models

class register(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    date_of_birth = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
class Login(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
class Logout(models.Model):
    token = models.CharField(max_length=255)
    
class suggest_book(models.Model):
    Authorization = models.CharField(max_length=255)
    seat = models.CharField(max_length=255)
# Create your models here.
