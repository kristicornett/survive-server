from django.db import models

class ZombieSightingStatusLog(models.Model):
    enteredUser = models.ForeignKey('Survivor', on_delete=models.CASCADE, related_name='entered user')
    enteredDate = models.DateField(blank=True)
    previousStatus = models.ForeignKey('ZombieSightingStatus', on_delete=models.CASCADE, related_name='previous status')
    newStatus = models.IntegerField(blank=True)
