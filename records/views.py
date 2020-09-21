from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect

from .models import CustomerModel
from .models import MilkModel
from .models import RecordsModel


class RecordsView(View):
    template_name = 'records/records.html'
    context = {}

    def get(self, request, *args, **kwargs):
        import datetime
        date = request.GET.get('date', None)
        if date is None:
            # date = datetime.datetime.now().date()
            self.context['records'] = RecordsModel.objects.all()
        else:
            date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            self.context['records'] = RecordsModel.objects.filter(date=date)
        return render(request, self.template_name, self.context)


class GenerateView(View):
    template_name = 'records/generate.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['customers'] = CustomerModel.objects.all()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        try:
            self.template_name = 'records/bill.html'
            customerid = request.POST.get('customer')
            date1 = request.POST.get('date1')
            date2 = request.POST.get('date2')
            cust_obj = CustomerModel.objects.get(pk=customerid)
            record_obj = RecordsModel.objects.filter(
                customer=cust_obj).filter(date__range=[date1, date2])
            total_price = 0
            for record in record_obj:
                total_price += record.amount
            self.context['customer'] = cust_obj
            self.context['records'] = record_obj
            self.context['days'] = len(record_obj)
            self.context['total_price'] = total_price
            return render(request, self.template_name, self.context)
        except Exception as e:
            self.template_name = 'records/generate.html'
            self.context['detail'] = 'Problem arise: ' + str(e)
            return render(request, self.template_name, self.context)


class EntryView(View):
    template_name = 'records/entry.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['customers'] = CustomerModel.objects.all()
        self.context['milks'] = MilkModel.objects.all()
        self.context['records'] = RecordsModel.objects.all()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        try:
            customerid = request.POST.get('customer')
            date = request.POST.get('date')
            milkid = request.POST.get('type')
            quantity = float(request.POST.get('quantity'))
            cust_obj = CustomerModel.objects.get(pk=customerid)
            milk_obj = MilkModel.objects.get(pk=milkid)
            amount = float(milk_obj.rate) * quantity
            RecordsModel.objects.create(
                customer=cust_obj, milk=milk_obj, quantity=quantity, date=date, amount=amount)
            self.context['detail'] = 'Successfully added.'
            return render(request, self.template_name, self.context)
        except Exception as e:
            self.context['detail'] = 'Problem arise: ' + str(e)
            return render(request, self.template_name, self.context)


class AddCustomerView(View):
    template_name = 'records/customer.html'
    context = {}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        try:
            name = request.POST.get('name')
            address = request.POST.get('address')
            mobile = request.POST.get('mobile')
            whatsapp = request.POST.get('whatsapp')
            CustomerModel.objects.create(
                name=name, address=address, mobile_no=mobile, whatsapp_no=whatsapp)
            self.context['detail'] = 'Customer: ' + \
                name + ' is successfully added.'
            return render(request, self.template_name, self.context)
        except Exception as e:
            self.context['detail'] = 'Problem arise: ' + str(e)
            return render(request, self.template_name, self.context)


class AddMilkView(View):
    template_name = 'records/milk.html'
    context = {}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        try:
            milk = request.POST.get('milk')
            rate = request.POST.get('rate')
            MilkModel.objects.create(milk_type=milk, rate=rate)
            self.context['detail'] = milk + \
                ' (Rs ' + str(rate) + ' per kg)' + ' is successfully added.'
            return render(request, self.template_name, self.context)
        except Exception as e:
            self.context['detail'] = 'Problem arise: ' + str(e)
            return render(request, self.template_name, self.context)
