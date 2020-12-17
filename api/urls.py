from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
#router.register(r'driver/register', views.DriverRegisterApIView)
# router.register(r'driver/:id/sendLocation',views.DriverLocationViewSet)



urlpatterns = [
    # path('driver/location/',views.DriverLocationViewSet.as_view(),name='driver_location'),
    path('',include(router.urls)),
    path('driver/register/', views.DriverRegisterApIView.as_view()),
    path('driver/<int:id>/sendLocation/', views.DriverLocationApIView.as_view()),
    # path('driver/list/',views.DriverList.as_view(),name='driver'),
    path('passenger/available_cabs/',views.DriverAPIView.as_view(),name='driverlist'),
    
]

