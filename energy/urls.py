from django.urls import path
#from . import views
from energy.views import BuildingView, RoomView, GraphView

urlpatterns = [
    path('', BuildingView.as_view(), name='building-view'),
    path('building/<int:pk>', RoomView.as_view(), name="room-view" ),
    path('graph/<int:pk>', GraphView.as_view(), name="graph-view"),
]

