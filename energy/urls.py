from django.urls import path
#from . import views
from energy.views import BuildingView, MeterView, GraphView

urlpatterns = [
    path('', BuildingView.as_view(), name='building-view'),
    path('<int:pk>/meters', MeterView.as_view(), name="meter-view" ),
    path('graph/<int:pk>', GraphView.as_view(), name="graph-view"),
]

