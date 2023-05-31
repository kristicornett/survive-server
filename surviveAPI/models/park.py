from django.db import models

class Park(models.Model):
    parkCode = models.CharField(max_length=10)
    description = models.CharField(max_length=350)