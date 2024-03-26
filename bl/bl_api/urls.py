from django.urls import path
from .views import (
    PlaceListApiView,
    ContinentList
)

urlpatterns = [
    path('list', PlaceListApiView.as_view()),
    path('<str:continent>', ContinentList.as_view())
]