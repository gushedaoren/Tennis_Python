import django
from django.db import models
import datetime
import django_filters


class Province(models.Model):

    id=models.BigIntegerField(primary_key=True);
    provinceName=models.TextField();


class City(models.Model):

    id=models.BigIntegerField(primary_key=True);
    cityName=models.TextField();
    provinceID=models.BigIntegerField();
   # pinyin=models.TextField();



class District(models.Model):

    districtID=models.BigIntegerField();
    districtName=models.TextField();
    id=models.BigIntegerField(primary_key=True);





class Court(models.Model):


    title = models.TextField()
    description = models.TextField()
    court_number=models.IntegerField(null=True);
    phone=models.TextField(null=True)
    court_level=models.TextField()
    address = models.TextField(null=True)

    price=models.TextField(null=True);
    province_model=models.ForeignKey(Province,related_name='province_model',null=True)
    city_model=models.ForeignKey(City,related_name='city_model',null=True)
    district_model=models.ForeignKey(District,related_name='district_model',null=True);


    class Meta:
        ordering = ('title',)

class User(models.Model):
    name=models.TextField();
    password=models.TextField();
    email=models.TextField(null=True);
    sex=models.IntegerField(null=True);  #man 0 woman 1
    age=models.IntegerField(null=True);
    address=models.TextField(null=True);




class Event(models.Model):
    title=models.TextField();
    content=models.TextField(null=True);
    address=models.TextField(null=True);
    level=models.IntegerField(null=True);  #man 0 woman 1
    phone=models.IntegerField(null=True);
    time=models.TextField(null=True);
    fee=models.TextField(null=True);
    remark=models.TextField(null=True);




