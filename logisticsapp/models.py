from django.db import models

# Create your models here.
class Quote(models.Model):
    city_departure = models.CharField(max_length=100)
    delivery_City = models.CharField(max_length=100)
    total_Weight = models.IntegerField()
    dimension = models.CharField(max_length=100)
    shipment_Type = models.CharField(max_length=100)
    urgency_Level = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField(max_length=100)
    additional_info = models.TextField()

    def __str__(self):
        return self.fullname
