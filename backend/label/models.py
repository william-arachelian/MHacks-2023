from django.db import models

# Create your models here.
class Label(models.Model):
    calories = models.IntegerField()
    total_fat = models.IntegerField()
    trans_fat = models.IntegerField()
    sat_fat = models.IntegerField()
    carbs = models.IntegerField()
    sugar = models.IntegerField()
    fiber = models.IntegerField()
    cholesterol = models.IntegerField()
    sodium = models.IntegerField()
    protein =  models.IntegerField()
    