from django.db import models

# Create your models here.
class Hotel(models.Model):
    name=models.CharField(max_length=250)
    rate=models.CharField( max_length=250)
    photo=models.ImageField(upload_to='mvpic')
    desc=models.TextField()
    
class Room(models.Model):
    name=models.CharField(max_length=250)
    rate=models.CharField( max_length=250)
    photo=models.ImageField(upload_to='mvpic')
    desc=models.TextField()