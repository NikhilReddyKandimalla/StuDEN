from django.db import models

# Create your models here.
class UserRegisterModel(models.Model):
    email = models.CharField(max_length=100)
    pswd = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    studentid = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)