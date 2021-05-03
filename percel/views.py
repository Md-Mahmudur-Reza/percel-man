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
            filled_form.save()
            note = "%s's %s product will be delivered"%(filled_form.cleaned_data['percel_id'], filled_form.cleaned_data['product_type'])
            new_form = ProductForms()
            context = {'product_form':new_form,'note':note}
            return render(request, 'percel/order.html', context)
    else:
        form = ProductForms()
        context = {'product_form':form}
        return render(request, 'percel/order.html', context)