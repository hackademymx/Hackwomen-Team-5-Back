from django.db import models

# Create your models here.


class Place(models.Model):
    name =  models.CharField(max_length=56)
    description = models.CharField(max_length=256)
    state = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    colonia = models.CharField(max_length=32)
    street = models.CharField(max_length=32)
    zipcode = models.CharField(max_length=32)
    
    class Meta:
        db_table = 'places'
    
    def __str__(self):
        return self.name
    
