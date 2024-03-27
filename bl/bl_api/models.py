from django.db import models
from django.contrib.auth.models import User

# class Todo(models.Model):
#     task = models.CharField(max_length = 180)
#     timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
#     completed = models.BooleanField(default = False, blank = True)
#     updated = models.DateTimeField(auto_now = True, blank = True)
#     user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

#     def __str__(self):
#         return self.task

class Continent(models.Model):
    continent_code = models.TextField(primary_key = True)
    continent_name = models.TextField(null = False)
    population = models.BigIntegerField()

class Country(models.Model):
    country_code = models.TextField(primary_key = True)
    continent_code = models.ForeignKey(Continent, on_delete = models.CASCADE)
    country_name = models.TextField(null = False)
    capital = models.TextField()
    population = models.IntegerField()


class City(models.Model):
    geoname_id = models.IntegerField(primary_key = True)
    city_name = models.TextField(null = False)
    alternate_names = models.TextField()
    country_code = models.ForeignKey(Country, on_delete = models.CASCADE)
    population = models.IntegerField()

class BucketList(models.Model):
    country = models.ForeignKey(Country, on_delete = models.CASCADE)
    city = models.ForeignKey(City, on_delete = models.CASCADE, blank = True)
    continent = models.ForeignKey(Continent, on_delete = models.CASCADE)
    activity = models.TextField() # TODO: add choices
    comment = models.TextField(null = True)
    traveled_from_city = models.TextField(blank = True)
    traveled_from_country = models.TextField(blank = True)
    # traveled_from = models.ForeignKey(City, on_delete = models.CASCADE, related_name = 'city_name', blank = True)
    traveled_via = models.TextField(blank = True) # TODO: add choices
    # when_visited = models.DateTimeField()
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    completed = models.BooleanField(default = False, blank = True)
    recommended = models.BooleanField(default = False, blank = True)
    rating = models.FloatField(default = 0, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
