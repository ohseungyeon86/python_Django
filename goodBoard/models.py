from django.db import models
from django.utils import timezone

# Create your models here.
class Boards(models.Model):
    no = models.AutoField(primary_key=True)
    id = models.CharField(models.ForeignKey("login", verbose_name="loginForeign", on_delete=models.CASCADE),max_length=10)
    title = models.CharField(max_length=30)
    content = models.TextField()
    photo = models.ImageField(blank=True)
    created = models.DateTimeField(default=timezone.now)

class login(models.Model):
    id = models.CharField(max_length=10,primary_key=True)
    password = models.CharField(max_length=30)
    created = models.DateTimeField(default=timezone.now)
   