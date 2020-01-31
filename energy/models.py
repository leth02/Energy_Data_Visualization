from django.db import models
from django.urls import reverse
import uuid

class Building(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50,help_text='Enter the name of the building')

    def __str__(self):
        return "Bulding ID: " + str(self.id) + ", Building name: " + self.name

    def get_absolute_url(self):
        return reverse("meter-view", args=[str(self.id)])


class Meter(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return "Meter ID: " + str(self.id) + ", meter name: " + self.name
    
    def get_absolute_url(self):
        return reverse("graph-view", args=[str(self.id)])

class Building_Meter(models.Model):
    building_id = models.ForeignKey(Building, on_delete = models.SET_NULL, null = True)
    meter_id = models.ForeignKey(Meter, on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return "this meter (" + str(self.meter_id) + ") belongs to (" + str(self.building_id) 

class Meter_dly(models.Model):
    year = models.CharField(max_length = 4)
    month = models.CharField(max_length = 2)
    day = models.CharField(max_length = 2)
    meter_id = models.ForeignKey(Meter, on_delete = models.SET_NULL, null = True)

    consumption = models.FloatField()

    def __str__(self):
        return f'{self.year}/{self.month}/{self.day}, {self.meter_id}, consumption: {self.consumption} + kWh'

