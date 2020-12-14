from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import viewsets
from .models import Driver,DriverLocation
from .serializers import DriverSerializer,DriverLocationSerializer,DriverListSerializer
from rest_framework.views import APIView
from .Harversigndist import Haversine
# Create your views here.
def index(request):
    return JsonResponse({"msg":"Cab App"})




class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class DriverLocationViewSet(viewsets.ModelViewSet):
    queryset = DriverLocation.objects.all()
    serializer_class = DriverLocationSerializer



# class DriverList(APIView):
#     def get(self,request,format=None):
#         pk=1
#         driver = Driver.objects.get(pk=pk)
#         driverlocation = DriverLocation.objects.filter(driver=driver)
#         serializer = DriverLocationSerializer(driverlocation,many=True)
#         return Response(serializer.data)
        

def driverlist(obj):
    longt,lat=obj
    data = DriverLocation.objects.all()
    dict ={}
    list=[]
    for i in data:
        dist=Haversine((lat,i.latitude),(longt,i.longitude)).km
        diverdict = {}
        if dist >=4:
            driver=Driver.objects.get(id=i.driver.id)
            diverdict["name"]=driver.name
            diverdict["car_number"] =driver.car_number
            diverdict["phone_number"] = driver.phone_number
            list.append(diverdict)
    return list

class DriverAPIView(CreateAPIView):
    serializer_class=DriverListSerializer
    def post(self,request,*args,**kwargs):
        if request.method=='POST':
            longt = float(request.data.get("longitude"))
            lat = float(request.data.get("latitude"))
            list=[longt,lat]        
            obj = driverlist(list)

            return JsonResponse({"availiable_cabs":obj})