from rest_framework import serializers
from .models import BucketList, Country, Continent, City

class BucketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BucketList
        fields = '__all__'

class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'