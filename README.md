# DJANGO-SPUTNIK-MAPS
## USAGE:
* include the ``django_sputnik_maps`` app in your settings.py
* create a model where the field names match the example 

```python
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
@admin.register(SampleModel)
class SampleModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        AddressField: {
            'widget': AddressWidget
        }
    }
``` 


