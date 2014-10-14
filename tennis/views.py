from django_filters import filters
from rest_framework import generics
from tennis.models import Court, City
from tennis.serializers import CourtSerializer, CitySerializer


class CourtList(generics.ListCreateAPIView):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer

    filter_fields = ('courtNumber','cityModel__cityID')




class CourtDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer





class CityList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer



class CityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


