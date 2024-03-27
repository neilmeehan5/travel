from django.urls import path
from .views import (
    PlaceListApiView,
    CityList,
    CountryList,
    Test,
    # InitContinents,
    # InitCountries,
    # InitCities,
    # ContinentList
)

urlpatterns = [
    path('list', PlaceListApiView.as_view()),
    path('test', Test.as_view()),
    # path('continents/init', InitContinents.as_view()),
    # path('countries/init', InitCountries.as_view()),
    # path('cities/init', InitCities.as_view()),
    path('<str:continent>/<str:country>', CityList.as_view()),
    path('<str:continent>', CountryList.as_view()),
]