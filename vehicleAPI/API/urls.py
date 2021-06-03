from django.conf.urls import url
from django.urls import path, include
from . import views
# refered from: https://bezkoder.com/django-rest-api/

urlpatterns = [ 
    url(r'^vehicles/(?P<pk>[\w]+)$', views.vehicle_detail),
    url(r'^vehicles/(?P<pk>[\w]+)/(?P<date>[\w]+)$', views.vehicle_detail),
]