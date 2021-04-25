from django.db import models

# Create your models here.
class IRB(models.Model):
    IRBpointer = models.ForeignKey(to='users.CustomUser',on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
