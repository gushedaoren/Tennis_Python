from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from tennis import views


urlpatterns = patterns('',
    url(r'^tennis/court_list$', views.CourtList.as_view()),
    url(r'^tennis/court_detial(?P<pk>[0-9]+)/$', views.CourtDetail.as_view()),
    url(r'^tennis/city_list$', views.CityList.as_view()),
    url(r'^tennis/city_detial(?P<pk>[0-9]+)/$', views.CityDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)