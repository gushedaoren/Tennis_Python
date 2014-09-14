from django.db import models





class BaseCity(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    cityName = models.TextField()
    cityType = models.TextField()
    isHot = models.BooleanField()
    firstLetter=models.TextField()

    class Meta:
        ordering = ('created',)

class Court(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    title = models.TextField()
    cityType = models.TextField()
    address = models.TextField()
    phone=models.TextField()
    startTime=models.TextField()
    endTime=models.TextField()
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



