from django.db import models

class ZombieSightingStatus(models.Model):
    status = models.CharField(max_length=155)