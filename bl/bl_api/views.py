from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Place, Continent, Country, City
from .serializers import PlaceSerializer, CountrySerializer, CitySerializer 
import geonamescache

# TODO: Probably should do this some other way...
# class InitContinents(APIView):
#     def get(self, request):
#         gc = geonamescache.GeonamesCache()
#         continents = gc.get_continents()

#         for continent in continents:
#             temp = Continent(continent_code = continent,
#                              continent_name = continents[continent]['name'],
#                              population = continents[continent]['population'])
#             temp.save()

#         return Response({'message': 'Successfully loaded continents!'}, status=status.HTTP_200_OK)
    
# class InitCountries(APIView):
#     def get(self, request):
#         gc = geonamescache.GeonamesCache()
#         countries = gc.get_countries()

#         for country in countries:
#             temp = Country(country_code = country,
#                            country_name = countries[country]['name'],
#                            continent_code = Continent.objects.filter(continent_code = countries[country]['continentcode']).first(),
#                            capital = countries[country]['capital'],
#                              population = countries[country]['population'])
#             temp.save()

#         return Response({'message': 'Successfully loaded countries!'}, status=status.HTTP_200_OK)
    
# class InitCities(APIView):
#     def get(self, request):
#         gc = geonamescache.GeonamesCache()
#         cities = gc.get_cities()

#         for city in cities:
#             temp = City(country_code = Country.objects.filter(country_code = cities[city]['countrycode']).first(),
#                         city_name = cities[city]['name'],
#                         alternate_names = cities[city]['alternatenames'],
#                         geoname_id = cities[city]['geonameid'],
#                              population = cities[city]['population'])
#             temp.save()

#         return Response({'message': 'Successfully loaded cities!'}, status=status.HTTP_200_OK)


class CountryList(APIView):
    def get(self, request, continent: str):
        countries = Country.objects.filter(continent_code = continent).order_by('-population')
        serializer = CountrySerializer(countries, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CityList(APIView):
    def get(self, request, country: str, continent: str):
        cities = City.objects.filter(country_code = country).order_by('-population')
        serializer = CitySerializer(cities, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PlaceListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        places = Place.objects.filter(user = request.user.id)
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = PlaceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)