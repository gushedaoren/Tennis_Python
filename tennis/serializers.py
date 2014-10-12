from rest_framework import serializers
from tennis.models import Court, City, District


class CitySerializer(serializers.ModelSerializer):


    class Meta:
        model = City
        fields = ('cityID', 'cityName', 'provinceID')


class DistrictSerializer(serializers.ModelSerializer):


    class Meta:
        model = District
        fields = ('cityID', 'districtName', 'cityID')

class CourtSerializer(serializers.ModelSerializer):
    cityModel=CitySerializer(source='cityModel')
    districtModel=DistrictSerializer(source='districtModel')

    class Meta:
        model = Court
        fields = ('id', 'title', 'description', 'courtNumber', 'phone', 'court_level','address','price',
       'cityModel','districtModel')