from django.db import models

class Supply(models.Model):
    name = models.CharField(max_length=40)
    supplyType = models.ForeignKey('SupplyType', on_delete=models.CASCADE, related_name='type')
    