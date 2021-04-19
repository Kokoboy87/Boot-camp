import datetime
from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Show title must be at least 2 characters"
        if len(postData['networks']) < 3:
            errors["networks"] = "Show networks must be at least 3 characters"
        if datetime.datetime.strptime(postData.get('release_date'), "%Y-%m-%d") >= datetime.datetime.today():
            errors["release_date"] = "Date must be in the past"
        if len(postData['description']) < 10:
            errors["description"] = "Show description must be at least 10 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    networks = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
