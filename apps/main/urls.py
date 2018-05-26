from django.conf.urls import url
from . import views   






       
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$',views.register),
    url(r'^login$',views.login),
    url(r'^logout$',views.logout),
    url(r'^destination/logout$',views.logout),
    #url(r'^travels$',views.travels),
    url(r'^dashboard$',views.dashboard),
    url(r'^destination/dashboard$',views.dashboard),
    url(r'^addtrip$',views.addtrip),
    url(r'^jointrip/(?P<trip_id>\d+)$',views.jointrip),
    url(r'^destination/jointrip/(?P<trip_id>\d+)$',views.destination),
    url(r'^destination/(?P<trip_id>\d+)$',views.destination),
    url(r'^add_trip$',views.add_trip)  # put in view
  ]
