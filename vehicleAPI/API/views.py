from itertools import count
from django.db.models import query
from django.db.models import FilteredRelation, Q
# from django.db.models.query_utils import FilteredRelation
from django.http import response, HttpResponse, QueryDict
from vehicleAPI.API.serializers import VehicleDistanceLogSerializer, VehicleSerializer
from vehicleAPI.models import Vehicle, VehicleDistanceLog
from .serializers import VehicleSerializer
from rest_framework import generics, renderers, status
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from datetime import datetime, timedelta
from django.http.multipartparser import MultiPartParser
from django.db.models import Max

# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Vehicle.objects.all()
#     renderer_classes = [renderers.StaticHTMLRenderer]

#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)

# class SnippetList(generics.ListCreateAPIView):
#     queryset = Vehicle.objects.all()
#     serializer_class = VehicleSerializer


# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Vehicle.objects.all()
#     serializer_class = VehicleSerializer

@api_view(['GET', 'POST'])
def vehicle_list(request):
    if request.method == 'GET':
        vehicles = Vehicle.objects.all()
        
        title = request.query_params.get('title', None)
        # if title is not None:
        #     vehicles = vehicles.filter(title__icontains=title)
        s = "2021-06-05"
        # .datetime.strptime(s, "%Y-%m-%d").date()
        date = datetime.strptime(s, "%Y-%m-%d").date() -timedelta(days=1)
        # w = Vehicle.objects.filter(distances__LogDate=date.strftime('%Y-%m-%d'))
        #     distances__LogDate = FilteredRelation(
        #         'distances__LogDate', condition=Q(distances__LogDate=True),
        #     )
        # )
        w = VehicleDistanceLog.objects.filter(LogDate=date.strftime('%Y-%m-%d'))

        # .filter(pizzas_vegetarian__name__icontains='mozzarella')
        tutorials_serializer = VehicleDistanceLogSerializer(w, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    # elif request.method == 'POST':
    #     tutorial_data = JSONParser().parse(request)
    #     tutorial_serializer = TutorialSerializer(data=tutorial_data)
    #     if tutorial_serializer.is_valid():
    #         tutorial_serializer.save()
    #         return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
    #     return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # elif request.method == 'DELETE':
    #     count = Tutorial.objects.all().delete()
    #     return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 

@api_view(['GET', 'PATCH'])
def vehicle_detail(request, pk, date = ''):
    # raise SystemExit


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
        # tutorials_serializer = VehicleDistanceLogSerializer(w, many=True)
        return JsonResponse(distance, safe=False)
 
    elif request.method == 'PATCH': 
        # vehicle_data = JSONParser().parse(request) 
        try: 
            vehicle = Vehicle.objects.get(pk=pk) 
        # return HttpResponse(str(vehicle)) 
        except Vehicle.DoesNotExist: 
            return JsonResponse({'message': 'The vehicle does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
        query_dict = request.POST
        vehicle_serializer = VehicleSerializer(vehicle, data=request.data, partial=True) 
        
        # vehicle_serializer = VehicleDistanceLogSerializer(vehicle, data=request.data, partial=True) 
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
 
    # elif request.method == 'DELETE': 
    #     tutorial.delete() 
    #     return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
       