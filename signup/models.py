from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    def __str__(self):
        return self.first_name+' '+ self.last_name+': '+self.email
