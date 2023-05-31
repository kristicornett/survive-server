from django.db import models

class Trade(models.Model):
     description = models.CharField(max_length=25)
     wanted = models.CharField(max_length=25)
     survivor = models.ForeignKey('Survivor', on_delete=models.CASCADE, related_name='enteredUser')
     supplyTypeOffer =  
     supplyTypeWanted =






"description": "Tampons",
        "wanted": "Batteries",
        "enteredUserId": 1,
        "supplyTypeOfferId": 7,
        "supplyTypeWantedId": 8,
        "townId": 1,
       
        "acceptedUserId": 2