from django.db import models

class ZombieSighting(models.Model):
    name = models.ForeignKey('Suvivor', on_delete=models.CASCADE, related_name='survivors')
    town = models.ForeignKey('Town', on_delete=models.CASCADE, related_name='towns')
    zombieSightingDistance = models.ForeignKey('ZombieSightingDistance', on_delete=models.CASCADE, related_name='zombie sighting distances')
    zombieSightingType = models.ForeignKey('ZombieSightingType', on_delete=models.CASCADE, related_name='zombie sighting types')
    approxCount = models.IntegerField(blank=True, null=True)
    enteredDate = models.DateField(blank=True, null=True)
    zombieSightingStatus = models.ForeignKey('ZombieSightingStatus', on_delete=models.CASCADE, related_name='zombie sighting statuses')
    
    