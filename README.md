# DJANGO-SPUTNIK-MAPS
## USAGE:
* include the ``django_sputnik_maps`` app in your settings.py
* create a model where the field names match the example 

```python
from django.db import models
from django_sputnik_maps.fields import AddressField


class SampleModel(models.Model):
    region = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house = models.IntegerField()
    lat = models.FloatField()
    lon = models.FloatField()
    address = AddressField(max_length=200)
```
* in the ``admin.py`` include the following as a formfield_override

```python
from django.contrib import admin
from django_sputnik_maps.fields import AddressField
from django_sputnik_maps.widgets import AddressWidget

from .models import SampleModel


@admin.register(SampleModel)
class SampleModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        AddressField: {
            'widget': AddressWidget
        }
    }
``` 


