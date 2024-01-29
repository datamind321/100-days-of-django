from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    pincode = models.IntegerField()
    resume = models.FileField(upload_to='uploads/')
    profile_image = models.ImageField(upload_to='uploads/',blank=True,default=None)
    cover_letter = models.FileField(blank=True,default='None',upload_to='uploads/')
    social_profile = models.URLField(default=None,blank=True)
    github_profile = models.URLField(default=None,blank=True)
    website = models.URLField(default=None,blank=True)
    skills = models.TextField()
    ac = models.BooleanField('Accept the terms and conditions',default=True)
