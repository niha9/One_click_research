from django.db import models

# Create your models here.
class Director_details(models.Model):
    director_id = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)

    def __str__(self):
         return str(self.director_id)
