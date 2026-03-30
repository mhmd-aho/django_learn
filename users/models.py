from django.db import models

# Create your models here.
class Country(models.Model):
    countryName = models.CharField(max_length=50)
    def __str__(self):
        return self.countryName
class User(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    nationality=models.ForeignKey(Country,on_delete= models.CASCADE,default=None)