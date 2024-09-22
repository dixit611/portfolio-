from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.
class CustomUser(models.Model):
# Create your models here.
  service_icon = models.CharField(max_length=50)
  service_title = models.CharField(max_length=50)
  service_description = models.TextField()
  user = models.ForeignKey(User, on_delete = models.SET_NULL, null= True , blank= True)

# class ContactFormSubmission(models.Model):
#     name = models.CharField(max_length=100)
#     mobile = models.CharField(max_length=15)
#     email = models.EmailField(max_length=100)
#     message = models.TextField()
#     website = models.URLField(max_length=200, blank=True)
#     submission_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name
class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    message = models.TextField()
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('minor', 'Minor'),
        ('major', 'Major'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title