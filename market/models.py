import datetime

from django.db import models
from users.models import User
from django.db.models.signals import post_save, pre_save, pre_delete
import csv
from django.dispatch import receiver




class Product(models.Model):
    name = models.CharField(max_length=20)
    cost = models.IntegerField()
    count = models.IntegerField()
    info_product = models.CharField(max_length=200, null=True, blank=True)
    # slug = models.SlugField()

    def __str__(self):
        return self.name


class Order(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField(null=True)
    order_datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Ticket(models.Model):
    uuid = models.UUIDField(unique=True)
    available = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

@receiver([post_save], sender=Order)
def order_csv(sender, instance: Order, **kwargs):
    with open("order.csv", "a", newline="") as csvfile:
        fieldnames = ["id", "name", "count", "order_datetime", "user"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({"id": instance.id,
                         "name": instance.products.name,
                         "count": instance.count,
                         # "cost": instance.count * Product.cost,
                         "order_datetime": instance.order_datetime.strftime("%H:%M %d.%m.%Y"),
                         "user": instance.user.username})