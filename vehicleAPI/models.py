from django.db import models

# Create your models here.
class Vehicle(models.Model):
    Unit = models.CharField(max_length=200, primary_key=True)
    Mileage = models.CharField(max_length=200)
    Manufacturer = models.CharField(max_length=200)
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.Unit + " " + self.Manufacturer

    class Meta:
        db_table = "vehicle"



#   python manage.py loaddata vehicle - this is to load the fixture
class VehicleDistanceLog(models.Model):
    Unit = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    CumilativeDistance = models.IntegerField()
    LogDate = models.DateField()

    def __str__(self):
        return self.Date + " " + self.CumilativeDistance

    class Meta:
        unique_together = (('Unit', 'LogDate'),)