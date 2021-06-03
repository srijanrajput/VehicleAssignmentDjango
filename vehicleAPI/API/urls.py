from django.conf.urls import url
from django.urls import path, include
from . import views
from django.views.generic.base import RedirectView
# refered from: https://bezkoder.com/django-rest-api/


urlpatterns = [ 
    url(r'^vehicles$', views.vehicle_list),
    url(r'^vehicles/(?P<pk>[\w]+)$', views.vehicle_detail),
    url(r'^vehicles/(?P<pk>[\w]+)/(?P<date>[\w]+)$', views.vehicle_detail),
]