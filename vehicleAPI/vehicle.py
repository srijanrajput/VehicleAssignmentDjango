from vehicleAPI.serializers import VehicleSerializer
from django.http import HttpResponse, JsonResponse, response
from rest_framework.response import Response
from .models import Vehicle

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Vehicle.objects.all()
#         serializer = VehicleSerializer(snippets)
#         return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)