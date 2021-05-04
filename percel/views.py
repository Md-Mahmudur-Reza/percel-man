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

            #LOGIC
            price = 0
            if str(model_destinations) == "Inside of Dhaka":
                print('Inside of Dhaka')
                price = 0
                if float(model_weight) >.5 and float(model_weight)<=2:
                    price = 60
                elif float(model_weight) >2 and float(model_weight)<=3:
                    price = 70
                elif float(model_weight) >3 and float(model_weight)<=4:
                    price = 80
                else:
                    price = 90

            elif str(model_destinations) == 'Division of Dhaka':
                print('Division of Dhaka')
                price = 0
                if float(model_weight) >.5 and float(model_weight)<=2:
                    price = 110
                elif float(model_weight) >2 and float(model_weight)<=3:
                    price = 130
                elif float(model_weight) >3 and float(model_weight)<=4:
                    price = 150
                else:
                    price = 170
                price = price + price*.01
                price = price + price*.5

            elif str(model_destinations) == 'Outside of Dhaka':
                print('Outside of Dhaka')
                price = 0
                if float(model_weight) >.5 and float(model_weight)<=2:
                    price = 130
                elif float(model_weight) >2 and float(model_weight)<=3:
                    price = 150
                elif float(model_weight) >3 and float(model_weight)<=4:
                    price = 170
                else:
                    price = 190
                price = price + price*.01
                price = price + price*.5

            context = {'name':model_name, 'product':model_products, 'weight': model_weight, 'destinations':model_destinations, 'prod_type':prod_type, 'price':price}
            Merchant.objects.get(id = PERCEL_NUMBER_PK).delete()
            return render(request, 'percel/invoice.html', context)
    else:
        form = ProductForms()
        context = {'product_form':form}
        return render(request, 'percel/order.html', context)

def invoice(request):
    return render (request, 'percel/invoice.html')