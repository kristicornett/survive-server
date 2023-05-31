from django.db import models

class ZombieSightingDistance(models.Model):
    distance = models.DecimalField(blank=True)