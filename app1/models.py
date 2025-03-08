from django.db import models

# Create your models here.


class Product(models.Model):
    product_id = models.CharField(max_length=100)
    invoice = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=255)
    booking_date = models.DateField()
    delivery_date = models.DateField()
    description = models.TextField()
    quantity = models.IntegerField()
    to_pay = models.DecimalField(max_digits=10, decimal_places=2)
    place = models.CharField(max_length=255)
    consignee_person = models.CharField(max_length=255)
    vehicle_number = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.product_id} - {self.receiver_name}"
