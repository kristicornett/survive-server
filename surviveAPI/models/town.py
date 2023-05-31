from django.db import models

class Town(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    population = models.IntegerField(blank=True, null=True)
    vacancy = models.BooleanField(blank=True, null=True)
    latitude = models.IntegerField(blank=True, null=True)
    longitude = models.IntegerField(blank=True, null=True)
    image = models.ImageField(blank=True)
    mapKey= models.CharField(max_length=100)