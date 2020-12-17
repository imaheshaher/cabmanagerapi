from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import viewsets
from .models import Driver,DriverLocation
from .serializers import DriverSerializer,DriverLocationSerializer,PassengerSerializer
from rest_framework.views import APIView
from .Harversigndist import Haversine
from rest_framework import status

# Create your views here.
def index(request):
    return JsonResponse({"msg":"Cab App"})


class DriverRegisterApIView(APIView):
    def get(self, request, format=None):
        snippets = Driver.objects.all()
        serializer = DriverSerializer(snippets, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"status":"failure","reason":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        #return Response(serializer.errors['email'], status=status.HTTP_400_BAD_REQUEST)



# class DriverViewSet(viewsets.ModelViewSet):
#     queryset = Driver.objects.all()
#     serializer_class = DriverSerializer

class DriverLocationApIView(APIView):
    def get(self, request, format=None,id=None):
        if id:
            snippets = DriverLocation.objects.filter(driver=1)
            serializer = DriverLocationSerializer(snippets,many=True)
            return Response(serializer.data)
        else:
            return Response({"stauts":'fail'})
    def post(self, request,format=None,id=None):
        serializer = DriverLocationSerializer(data=request.data)
        instance = self.get_object()
        print(instance)

        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success"} ,status=status.HTTP_202_ACCEPTED)
        return Response({"status":"failure","reason":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

# class DriverLocationViewSet(viewsets.ModelViewSet):
#     queryset = DriverLocation.objects.all()
#     serializer_class = DriverLocationSerializer



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
    serializer_class=PassengerSerializer
    def post(self,request,*args,**kwargs):
        if request.method=='POST':
            longt = float(request.data.get("longitude"))
            lat = float(request.data.get("latitude"))
            list=[longt,lat]        
            obj = driverlist(list)

            return JsonResponse({"availiable_cabs":obj})

