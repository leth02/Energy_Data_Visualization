from django.shortcuts import render
from energy.models import Building, Building_Meter, Meter, Meter_dly
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.views.generic import DetailView
from django.core import serializers


class BuildingView(ListView):
    model = Building
    context_object_name = "my_building_list"
    template_name = "buildingView.html"

class MeterView(ListView):
    #model = Room
    context_object_name = "my_meter_list"
    template_name = "meterView.html"

    def get_queryset(self):
        #self.building = get_object_or_404(Building, id = self.kwargs['pk'])
        self.building_meters = get_list_or_404(Building_Meter, building_id = self.kwargs['pk'])
        id_list = []
        for building_meter in self.building_meters:
            id_list.append(building_meter.meter_id.id)
        print(id_list)
        return Meter.objects.filter(id__in = id_list)

class GraphView(ListView):
    context_object_name = "meter_data"
    template_name = "graph.html"

    def get_queryset(self):
        #self.meter_id = get_object_or_404(Room, id = self.kwargs['pk'])
        get_data_set = Meter_dly.objects.filter(meter_id = self.kwargs['pk'])
        data_JSON = serializers.serialize("json", get_data_set)
        return data_JSON

