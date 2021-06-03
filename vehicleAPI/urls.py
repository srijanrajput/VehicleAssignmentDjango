from vehicleAPI import vehicle
from django.urls import path, include
from rest_framework import routers
from . import views

# urlpatterns = [
#     # path('', vehicle.index, name='index'),
#     path('', vehicle.snippet_list),

# ]


# router = routers.DefaultRouter()
# router.register(r'vehicles', views.VehicleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('vehicleAPI.API.urls')),
]