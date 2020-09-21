from django.db import models

import datetime
import uuid

# Create your models here.


class CustomerModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    address = models.TextField(default="", blank=True)
    mobile_no = models.CharField(max_length=10, blank=True)
    whatsapp_no = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name


class MilkModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    milk_type = models.CharField(verbose_name="Milk Type", max_length=30, choices=(
        ("Cow", "Cow"),
        ("Buffalo", "Buffalo")
    ))
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['rate', ]
        unique_together = ('milk_type', 'rate')

    def __str__(self):
        return self.milk_type + ' (Rs ' + str(self.rate) + ' per kg)'


class RecordsModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(
        CustomerModel, on_delete=models.CASCADE)
    milk = models.ForeignKey(
        MilkModel, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateField(default=datetime.date.today, blank=True, null=True)

    class Meta:
        ordering = ['-date', ]
