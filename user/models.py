from django.db import models
from django.core.validators import int_list_validator

# Create your models here.

class coders(models.Model):
    username = models.CharField(max_length=50)
    pic = models.URLField(max_length=250, null=True, default=None)
    location = models.CharField(max_length=50, null=True, default=None)
    workType = models.CharField(max_length=100, null=True, default=None)
    position = models.CharField(max_length=50, null=True, default=None)
    industryType = models.CharField(max_length=100, null=True, default=None)
    skillType = models.CharField(max_length=100, null=True, default=None)
    email = models.EmailField(max_length=50,null=True, default=None)
    github = models.URLField(max_length=250, null=True, default=None)
    linkedin = models.URLField(max_length=250, null=True, default=None)
    stackoverflow = models.URLField(max_length=250, null=True, default=None)
    phone = models.CharField(max_length=50,null=True, default=None)
    intro = models.CharField(max_length=1000, null=True, default=None)
    # location and timezone will be left null so far
    

class experienceInfo(models.Model):
    name = models.CharField(max_length=50)
    field = models.CharField(max_length=50)
    detail = models.CharField(max_length=1000, null=True, default=None)
    coder = models.ForeignKey(to=coders, related_name="experience", null=True, blank=True, default=None,
                                 on_delete=models.CASCADE)

class projectInfo(models.Model):
    name = models.CharField(max_length=50)
    field = models.CharField(max_length=50)
    detail = models.CharField(max_length=1000, null=True, default=None)
    coder = models.ForeignKey(to=coders, related_name="project", null=True, blank=True, default=None,
                                 on_delete=models.CASCADE)
