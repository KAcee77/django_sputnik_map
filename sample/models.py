from django.db import models
from django_sputnik_maps.fields import AddressField

# all fields must be present in the model
class SampleModel(models.Model):
    region = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house = models.IntegerField()
    lat = models.FloatField()
    lon = models.FloatField()
    address = AddressField(max_length=200)
    
