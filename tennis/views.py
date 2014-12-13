from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django_filters import filters
from rest_framework import generics

from tennis.models import Court, City,User
from tennis.serializers import CourtSerializer, CitySerializer, UserSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication
from rest_framework import exceptions



class CourtList(generics.ListCreateAPIView):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer

    filter_fields = ('court_number','province_model__id','city_model__id','district_model__id')




class CourtDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer





class CityList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer



class CityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer



class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class =UserSerializer



class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



def tennis_login(request):

        """

        :param request:
        :return: :raise exceptions.AuthenticationFailed:
        """


        username = request.GET['username']
        print("username:"+username)
        if not username:
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)



