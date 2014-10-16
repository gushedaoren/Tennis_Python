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
    courtNumber=models.IntegerField(null=True);
    phone=models.TextField(null=True)
    court_level=models.TextField()
    address = models.TextField(null=True)

    price=models.TextField(null=True);
    cityModel=models.ForeignKey(City,related_name='city',null=True)
    districtModel=models.ForeignKey(District,related_name='district',null=True);


    class Meta:
        ordering = ('title',)


