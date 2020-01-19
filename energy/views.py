from django.shortcuts import render
from energy.models import Room, Building, Energy
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.core import serializers

""" def index(request):

    num_bulding = Building.objects.all().count()
    
    context = {
        'num_building': num_bulding,
    }
    
    return render(request, 'index.html', context = context ) """

class BuildingView(ListView):
    model = Building
    context_object_name = "my_building_list"
    template_name = "buildingView.html"

class RoomView(ListView):
    #model = Room
    context_object_name = "my_room_list"
    template_name = "roomView.html"

    def get_queryset(self):
        self.buildingId = get_object_or_404(Building, id = self.kwargs['pk'])

        return Room.objects.filter(building = self.buildingId)

class GraphView(ListView):
    context_object_name = "room_data"
    template_name = "graph.html"

    def get_queryset(self):
        self.roomId = get_object_or_404(Room, id = self.kwargs['pk'])
        a = Energy.objects.filter(room = self.roomId)
        data = serializers.serialize("json", a)
        return data

