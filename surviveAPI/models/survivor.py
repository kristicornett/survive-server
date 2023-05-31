from django.db import models
from django.contrib.auth.models import User

class Survivor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    town = models.ForeignKey('Town', on_delete=models.CASCADE, related_name='survivor_town')

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    @property
    def email(self):
        return f'{self.user.email}'