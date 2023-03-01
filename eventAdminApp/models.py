from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class gallery(models.Model):
    eventName = models.CharField(max_length=200)
    eventPlace = models.CharField(max_length=100)
    eventDescription = models.CharField(max_length=1000)
    eventDate = models.DateField()
    eventImageOne = models.ImageField(upload_to="user/", null=True, default=None)
    eventImageTwo = models.ImageField(upload_to="user/", null=True, default=None)
    eventImageThree = models.ImageField(upload_to="user/", null=True, default=None)

class images(models.Model):
    pass



class Services(models.Model):
    serviceImage = models.ImageField(upload_to="Services/", null=True, default=None)
    eventTitle = models.CharField(max_length=300)
    


class videoContent(models.Model):
    eventName = models.CharField(max_length=200)
    eventCaption = models.CharField(max_length=200)
    video = EmbedVideoField() # same like models.URLField()



class contactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    number = models.CharField(max_length=13)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True)