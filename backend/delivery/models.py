from django.db import models
from orders.models import Order

# Create your models here.

class DeliveryInfo(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='delivery_info')
    address = models.CharField(max_length=255)
    delivery_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, default='pending')

    def __str__(self):
        return f"Delivery for {self.order}"
