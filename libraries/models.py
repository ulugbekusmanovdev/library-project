from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
