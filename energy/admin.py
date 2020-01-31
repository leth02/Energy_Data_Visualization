from django.contrib import admin
from .models import Building, Building_Meter, Meter, Meter_dly

admin.site.register(Building)
admin.site.register(Building_Meter)
admin.site.register(Meter)
admin.site.register(Meter_dly)