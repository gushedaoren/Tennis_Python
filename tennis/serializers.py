from rest_framework import serializers
from tennis.models import Court, City, District, Province,User,Event


class ProvinceSerializer(serializers.ModelSerializer):


    class Meta:
        model = Province
        fields = ('id', 'provinceName')


class CitySerializer(serializers.ModelSerializer):


    class Meta:
        model = City
        fields = ('id', 'cityName')


class DistrictSerializer(serializers.ModelSerializer):


    class Meta:
        model = District
        fields = ('id', 'districtName')

class CourtSerializer(serializers.ModelSerializer):
    province_model=ProvinceSerializer(source='province_model')
    city_model=CitySerializer(source='city_model')
    district_model=DistrictSerializer(source='district_model')

    class Meta:
        model = Court
        fields = ('id', 'title', 'description', 'court_number', 'phone', 'court_level','address','price',
       'province_model','city_model','district_model')


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('id', 'account','name','email','sex','age','address','phone','level')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=('id','title','description','address','phone','level','time','fee','remark')