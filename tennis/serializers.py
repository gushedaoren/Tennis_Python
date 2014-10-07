from rest_framework import serializers
from tennis.models import Court, BaseCity


class BaseCitySerializer(serializers.ModelSerializer):


    class Meta:
        model = BaseCity
        fields = ('id', 'cityName', 'cityType', 'firstLetter', 'isHot')


class CourtSerializer(serializers.ModelSerializer):
    city_BaseCity_Model=BaseCitySerializer(source='city_BaseCity_Model')
    district_BaseCity_Model=BaseCitySerializer(source='district_BaseCity_Model')

    class Meta:
        model = Court
        fields = ('id', 'title', 'cityType', 'address', 'phone', 'startTime','endTime','fee','courtDesc','courtCount','weight',
        'longitude','latitude','city_BaseCity_Model','district_BaseCity_Model')