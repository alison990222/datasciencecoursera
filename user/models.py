from django.db import models
from django.utils import timezone
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

class application(models.Model):
    time = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, null=True, default=None)
    coder = models.ForeignKey(to=coders, related_name="coder", null=True, blank=True, default=None,
                                 on_delete=models.CASCADE)
    company = models.ForeignKey(to=company, related_name="company", null=True, blank=True, default=None,
                                 on_delete=models.CASCADE)
    feedback = models.CharField(max_length=1000, null=True, default=None)
 


class company(models.Model):
    name = models.CharField(max_length=50, null=True, default=None)
    industry = models.CharField(max_length=50, null=True, default=None)
    location = models.CharField(max_length=50, null=True, default=None)
    foundDate = models.DateTimeField(default=timezone.now)
    companySize = models.CharField(max_length=50, null=True, default=None)
    fundingType = models.CharField(max_length=50, null=True, default=None)
    jobType = models.CharField(max_length=100, null=True, default=None)
    intro = models.CharField(max_length=1000, null=True, default=None)

    description = models.CharField(max_length=1000, null=True, default=None)
    vision = models.CharField(max_length=1000, null=True, default=None)
    companyVisit = models.CharField(max_length=1000, null=True, default=None)
    vision = models.CharField(max_length=1000, null=True, default=None)
    teamMeeting = models.CharField(max_length=1000, null=True, default=None)

    email = models.EmailField(max_length=50,null=True, default=None)
    twitter = models.URLField(max_length=250, null=True, default=None)
    linkedin = models.URLField(max_length=250, null=True, default=None)
    facebook = models.URLField(max_length=250, null=True, default=None)
    ins = models.URLField(max_length=250, null=True, default=None)


class Job(models.Model):
    name = models.CharField(max_length=50, null=True, default=None)
    


class experienceInfo(models.Model):
    name = models.CharField(max_length=50, null=True, default=None)
    field = models.CharField(max_length=50, null=True, default=None)
    time = models.DateTimeField(default=timezone.now)
    link = models.URLField(max_length=250, null=True, default=None)
    detail = models.CharField(max_length=1000, null=True, default=None)
    coder = models.ForeignKey(to=coders, related_name="experience", null=True, blank=True, default=None,
                                 on_delete=models.CASCADE)

class projectInfo(models.Model):
    name = models.CharField(max_length=50)
    field = models.CharField(max_length=50)
    time = models.DateTimeField(default=timezone.now)
    github = models.URLField(max_length=250, null=True, default=None)
    detail = models.CharField(max_length=1000, null=True, default=None)
    coder = models.ForeignKey(to=coders, related_name="project", null=True, blank=True, default=None,
                                 on_delete=models.CASCADE)

