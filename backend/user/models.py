from django.db import models

# Create your models here.
class User(models.Model):
    weight = models.IntegerField()
    height = models.IntegerField()
    age = models.IntegerField()
    sex = models.TextField()