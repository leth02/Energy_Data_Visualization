from django.contrib import admin
from .models import Energy, Room, Building

admin.site.register(Energy)
admin.site.register(Room)
admin.site.register(Building)