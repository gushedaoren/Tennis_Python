from rest_framework import serializers
from tennis.models import Court, City, District


class CitySerializer(serializers.ModelSerializer):


    class Meta:
        model = City
        fields = ('id', 'cityName')


class DistrictSerializer(serializers.ModelSerializer):


    class Meta:
        model = District
        fields = ('id', 'districtName')

class CourtSerializer(serializers.ModelSerializer):
    cityModel=CitySerializer(source='cityModel')
    districtModel=DistrictSerializer(source='districtModel')

    class Meta:
        model = Court
        fields = ('id', 'title', 'description', 'courtNumber', 'phone', 'court_level','address','price',
       'cityModel','districtModel')