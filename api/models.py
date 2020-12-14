from django.db import models

# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10,unique=True)
    license_number = models.CharField(max_length=50,unique=True)
    car_number = models.CharField(max_length=20,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class DriverLocation(models.Model):
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=15,decimal_places=8)
    longitude = models.DecimalField(max_digits=15,decimal_places=8)
    created_at = models.DateTimeField(auto_now_add=True)