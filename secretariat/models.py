from django.db import models

# Create your models here.
class sec_details(models.Model):

    designation = models.CharField(max_length=100)
    sec_id = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)

    def __str__(self):
         return str(self.sec_id)
