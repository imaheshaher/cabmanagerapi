from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.DriverViewSet)
router.register(r'd/location',views.DriverLocationViewSet)


urlpatterns = [
    # path('driver/location/',views.DriverLocationViewSet.as_view(),name='driver_location'),
    path('',include(router.urls)),
    # path('driver/list/',views.DriverList.as_view(),name='driver'),
    path('pasnger/list/',views.DriverAPIView.as_view(),name='driverlist'),
    
]

