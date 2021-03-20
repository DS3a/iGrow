from django.db import models

class Value(models.Model):
    Temperature = models.CharField(max_length=50)
    Pressure = models.CharField(max_length=50)
    Humidity = models.CharField(max_length=50)
    pH = models.CharField(max_length=50)
    Intensity = models.CharField(max_length=50)

    def __str__(self):
        return self.Temperature
# Create your models here.
