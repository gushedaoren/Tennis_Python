
from rest_framework import generics
from tennis.models import Court, BaseCity
from tennis.serializers import CourtSerializer, BaseCitySerializer


class CourtList(generics.ListCreateAPIView):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer

class CourtDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer



class CityList(generics.ListCreateAPIView):
    queryset = BaseCity.objects.all()
    serializer_class = BaseCitySerializer



class CityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BaseCity.objects.all()
    serializer_class = BaseCitySerializer