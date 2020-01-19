from django.db import models
from django.urls import reverse
import uuid

class Building(models.Model):
    name = models.CharField(max_length=50,help_text='Enter the name of the building')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("room-view", args=[str(self.id)])

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for each room of the building")
    title = models.CharField(max_length=30)
    building = models.ForeignKey(Building, on_delete = models.SET_NULL, null=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('graph-view', args = [str(int(self.id))])

class Energy(models.Model):
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null = True)
    date = models.CharField(max_length=10)
    time = models.CharField(max_length=5)
    electric = models.FloatField(null=True)
    heat = models.FloatField(null=True)

    def __str__(self):
        return f'{self.room}, {self.date}, {self.time}, {self.electric} kwH, {self.heat} F'