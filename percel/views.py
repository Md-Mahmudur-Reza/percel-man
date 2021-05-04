from django.shortcuts import render, HttpResponse
from .forms import MerchantForms, ProductForms
from .models import Merchant

def index(request):
    if request.method == 'POST':
        filled_form = MerchantForms(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = "%s, your percel  is saved"%(filled_form.cleaned_data['name'])
            new_form = MerchantForms()
            return render(request, 'percel/index.html', {'merchantform':new_form, 'note':note})
    else:
        form = MerchantForms()
        return render(request, 'percel/index.html', {'merchantform':form})



def  order(request):
    if request.method == 'POST':
        filled_form = ProductForms(request.POST)
        if filled_form.is_valid():
            nam = filled_form.cleaned_data['percel_id']
            PERCEL = Merchant.objects.get(name=nam)
            PERCEL_NUMBER_PK = PERCEL.pk

            model_obj = Merchant.objects.get(id = PERCEL_NUMBER_PK)

            model_name = model_obj.name
            model_products = model_obj.products
            model_weight = model_obj.total_weight
            model_destinations = model_obj.destinations

            prod_type = filled_form.cleaned_data['product_type']

            # PERCEL_NUMBER = filled_form.cleaned_data['percel_id']
            filled_form.save()
            #note = "%s's %s product will be delivered"%(filled_form.cleaned_data['percel_id'], filled_form.cleaned_data['product_type'])
            # new_form = ProductForms()
            #context = {'product_form':new_form}
            # context = {'percel_number':PERCEL_NUMBER_PK, 'obj':model_obj}
            context = {'name':model_name, 'product':model_products, 'weight': model_weight, 'destinations':model_destinations, 'prod_type':prod_type}
            return render(request, 'percel/invoice.html', context)
    else:
        form = ProductForms()
        context = {'product_form':form}
        return render(request, 'percel/order.html', context)

def invoice(request):
    context = {'percel_number':PERCEL_NUMBER}
    return render (request, 'percel/invoice.html', context)