from rest_framework import serializers
from tennis.models import Court, BaseCity, City


class CitySerializer(serializers.ModelSerializer):


    class Meta:
        model = City
        fields = ('CityID', 'CityName', 'ProvinceID')


class CourtSerializer(serializers.ModelSerializer):
    city_BaseCity_Model=CitySerializer(source='city_BaseCity_Model')
    district_BaseCity_Model=CitySerializer(source='district_BaseCity_Model')

    class Meta:
        model = Court
        fields = ('id', 'title', 'cityType', 'address', 'phone', 'startTime','endTime','fee','courtDesc','courtCount','weight',
        'longitude','latitude','city_BaseCity_Model','district_BaseCity_Model')