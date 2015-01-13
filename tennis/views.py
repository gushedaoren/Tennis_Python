from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django_filters import filters
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from tennis.models import Court, City,User,Event
from tennis.serializers import CourtSerializer, CitySerializer, UserSerializer,EventSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication
from rest_framework import exceptions

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

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



class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class =EventSerializer



class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

def login(request):

        account = request.GET['account']
        password = request.GET['password']
        print("account:"+account)

        if not account:
            return HttpResponse('{"statusCode":"2","message":"username is null"}')

        try:
            user = User.objects.get(account=account)

            if (user.account==account and user.password==password):
                return HttpResponse('{"statusCode":"0","message":"auth success"}')
            else :
                return HttpResponse('{"statusCode":"1","message":"auth failed"}')

        except User.DoesNotExist:

            user=None
            return HttpResponse('{"statusCode":"3","message":"no such user"}')

        return HttpResponse('{"statusCode":"1","message":"auth failed"}')







def register(request):

        account = request.GET['account']
        password = request.GET['password']
        sex = request.GET['sex']
        print("account:"+account)

        if not account:
          return HttpResponse('{"statusCode":"2","message":"username is null"}')

        try:

            user=User.objects.get(account=account);


            return HttpResponse('{"statusCode":"1","message":"user alreadly exits"}')

        except User.DoesNotExist:

            User.objects.create(account=account,password=password,sex=sex)





            return HttpResponse('{"statusCode":"0","message":"register success"}')




        return HttpResponse('{"statusCode":"1","message":"register failed"}')



def postEvent(request):

    title = request.GET.get('title')
    description = request.GET.get('description')
    address = request.GET.get('address')
    level = request.GET.get('level')
    phone = request.GET.get('phone')
    time = request.GET.get('time')
    fee = request.GET.get('fee')
    remark = request.GET.get('remark')


    event=Event.objects.create(title=title,description=description,address=address,level=level,phone=phone,time=time,fee=fee,remark=remark);

    return HttpResponse('{"statusCode":"0","message":"post event success"}')




def updateUserInfo(request):

     account=request.GET.get('account')
     name = request.GET.get('name')
     email = request.GET.get('email')
     sex = request.GET.get('sex')
     level = request.GET.get('level')
     age = request.GET.get('age')
     address = request.GET.get('address')
     phone = request.GET.get('phone')
     user=User.objects.get(account=account)
     user.name=name
     user.email=email
     user.sex=sex
     user.level=level
     user.age=age
     user.address=address
     user.phone=phone

     user.save()
     #User.objects.update(account=account,name=name,email=email,sex=sex,level=level,age=age,address=address,phone=phone);
     return HttpResponse('{"statusCode":"0","message":"update user success"}')
