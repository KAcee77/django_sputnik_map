# from django.db import models
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

