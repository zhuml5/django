from django.db import models

# Create your models here.
from django.utils import timezone

class Post(models.Model):
    mn = models.CharField(max_length=25)
    collect_time = models.CharField(max_length=50)
    create_time = models.CharField(max_length=50)
    do = models.CharField(max_length=20,default=0)
    temp = models.CharField(max_length=20,default=0)
    cod = models.CharField(max_length=20,default=0)
    cond = models.CharField(max_length=20,default=0)
    ph = models.CharField(max_length=20,default=0)
    nh3 = models.CharField(max_length=20,default=0)
    tp = models.CharField(max_length=20,default=0)
    orp = models.CharField(max_length=20,default=0)
    zd = models.CharField(max_length=20,default=0)

class User(models.Model):
    mn = models.CharField(max_length=25)
    detial = models.CharField(max_length=100,default=0)
