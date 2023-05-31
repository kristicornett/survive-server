from django.db import models

class ZombieSightingType(models.Model):
    type = models.CharField(max_length=20)
    image = models.ImageField(blank=True, null=True)
