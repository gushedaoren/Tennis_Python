import django
from django.db import models
import datetime


class Province(models.Model):

    ProvinceID=models.BigIntegerField();
    ProvinceName=models.TextField();


class City(models.Model):

    CityID=models.BigIntegerField();
    CityName=models.TextField();
    ProvinceID=models.BigIntegerField();



class District(models.Model):

    DistrictID=models.BigIntegerField();
    DistrictName=models.TextField();
    CityID=models.BigIntegerField();

class BaseCity(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    cityName = models.TextField()
    cityType = models.TextField()
    isHot = models.BooleanField(default=False)
    firstLetter=models.TextField()


    class Meta:
        ordering = ('created',)



class Court(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    title = models.TextField()
    cityType = models.TextField()
    address = models.TextField()
    phone=models.TextField()
    startTime=models.DateTimeField(auto_now_add=True)
    endTime=models.DateTimeField(auto_now_add=True)
    fee=models.TextField()
    courtDesc=models.TextField()
    courtCount=models.IntegerField()
    weight=models.IntegerField()
    longitude=models.FloatField()
    latitude=models.FloatField()
    city_BaseCity_Model=models.ForeignKey(BaseCity,related_name='city')
    district_BaseCity_Model=models.ForeignKey(BaseCity,related_name='district')


    class Meta:
        ordering = ('created',)



