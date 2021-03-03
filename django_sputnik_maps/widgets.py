from django.conf import settings
from django.forms import widgets


class AddressWidget(widgets.TextInput):
    '''a map will be drawn after the address field'''
    template_name = 'django_sputnik_maps/widgets/mapwidget.html'

    class Media:
        css = {
            'all': ('https://unpkg.com/leaflet@1.0.1/dist/leaflet.css',
                    settings.STATIC_URL + 'django_sputnik_maps/css/jquery-ui.min.css',
                    settings.STATIC_URL + 'django_sputnik_maps/css/base.css',)

        }
        js=(
            "https://unpkg.com/leaflet@1.0.1/dist/leaflet.js",
            settings.STATIC_URL + 'django_sputnik_maps/js/base.js',
            settings.STATIC_URL + 'django_sputnik_maps/js/jquery-3.5.1.js',
            settings.STATIC_URL + 'django_sputnik_maps/js/jquery-ui.min.js',
        )

