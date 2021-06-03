from vehicleAPI.API.serializers import VehicleDistanceLogSerializer, VehicleSerializer
from vehicleAPI.models import Vehicle, VehicleDistanceLog
from .serializers import VehicleSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from django.http.response import JsonResponse
from datetime import datetime, timedelta
from django.db.models import Max

@api_view(['GET'])
def vehicle_list(request):
     if request.method == 'GET': 
        vehicles = Vehicle.objects.all()
        vehicles = VehicleSerializer(vehicles, many=True)
        return JsonResponse(vehicles.data, safe=False)

@api_view(['GET', 'PATCH'])
def vehicle_detail(request, pk, date = ''):
    if request.method == 'GET': 
        try:
            given_date = datetime.strptime(date, "%Y%m%d").date()
            previous_date = given_date-timedelta(days=1)
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

        log_day_minus1 = VehicleDistanceLog.objects.filter(LogDate=previous_date.strftime('%Y-%m-%d'))
        if log_day_minus1.count() < 1:
            log_given_day = VehicleDistanceLog.objects.filter(LogDate=given_date.strftime('%Y-%m-%d')).filter(Unit=pk)

            if log_given_day.count() == 0:
                raise NotFound(detail="The data for given inputs does not exists", code=None)


        max_date = VehicleDistanceLog.objects.filter(
                        Unit=pk
                    ).aggregate(LogDate=Max('LogDate'))['LogDate']



        max_VehicleDistanceLog = VehicleDistanceLog.objects.filter(Unit=pk, LogDate=max_date.strftime('%Y-%m-%d'))
        distance = 0
        if log_day_minus1.count() > 0:
            distance = abs(log_day_minus1[0].CumilativeDistance - max_VehicleDistanceLog[0].CumilativeDistance)
        else:
            distance = max_VehicleDistanceLog[0].CumilativeDistance
        return JsonResponse(distance, safe=False)
 
    elif request.method == 'PATCH': 
        try: 
            vehicle = Vehicle.objects.get(pk=pk) 
        # return HttpResponse(str(vehicle)) 
        except Vehicle.DoesNotExist: 
            return JsonResponse({'message': 'The vehicle does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
        query_dict = request.POST
        vehicle_serializer = VehicleSerializer(vehicle, data=request.data, partial=True) 
        
        if vehicle_serializer.is_valid(): 

            cd = query_dict['CumilativeDistance']
            v1 = VehicleDistanceLog(
                Unit=vehicle,
                CumilativeDistance=cd,
                LogDate=datetime.now() + timedelta(days=3)
            )
            vehicle_serializer.save() 

            
            v1.save(force_insert=True)

            return JsonResponse(vehicle_serializer.data) 
        return JsonResponse(vehicle_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 