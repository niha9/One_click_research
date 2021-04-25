from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    TYPE_CHOICES = (
        (0,'DIRECTOR'),
        (1,'SECRETARIAT'),
        (2,'GUIDE'),
        (3,'STUDENT'),
        (4,'COINVESTIGATOR'),
        (5,'IRBMEMBERS'),
    )
    name = models.CharField(max_length=250)
    type = models.IntegerField(choices=TYPE_CHOICES, default=3)
    contact = models.IntegerField(default=100)

    def _str_(self):
        return str(self.username)
