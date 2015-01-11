from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from tennis import views


urlpatterns = patterns('',
    url(r'^tennis/court_list$', views.CourtList.as_view()),
    url(r'^tennis/court_detial(?P<pk>[0-9]+)/$', views.CourtDetail.as_view()),
    url(r'^tennis/city_list$', views.CityList.as_view()),
    url(r'^tennis/city_detial(?P<pk>[0-9]+)/$', views.CityDetail.as_view()),
    url(r'^tennis/user_list$', views.UserList.as_view()),
    url(r'^tennis/login$', views.login),
    url(r'^tennis/register', views.register),
    url(r'^tennis/post_event', views.postEvent),
    url(r'^tennis/event_list$', views.EventList.as_view()),
    url(r'^tennis/event_detial(?P<pk>[0-9]+)/$', views.EventDetail.as_view()),
     url(r'^tennis/update_userinfo', views.updateUserInfo),



)


urlpatterns = format_suffix_patterns(urlpatterns)