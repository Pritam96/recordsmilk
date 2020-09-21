from django.contrib import admin

from .models import CustomerModel
from .models import MilkModel
from .models import RecordsModel

# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile_no', 'whatsapp_no', 'address')


admin.site.register(CustomerModel, CustomerAdmin)


class MilkAdmin(admin.ModelAdmin):
    list_display = ('milk_type', 'rate')


admin.site.register(MilkModel, MilkAdmin)


class RecordsAdmin(admin.ModelAdmin):
    list_display = ('date', 'customer', 'milk',
                    'quantity', 'amount', 'created_at')


admin.site.register(RecordsModel, RecordsAdmin)
