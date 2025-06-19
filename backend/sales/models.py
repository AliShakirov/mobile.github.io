from django.db import models
from catalog.models import Product

class Sale(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    discount_percent = models.PositiveIntegerField()
    products = models.ManyToManyField(Product, related_name='sales')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title
