from django.shortcuts import render, HttpResponse
from .forms import MerchantForms

def index(request):
    # return HttpResponse("nothing")
    # return render(request, 'percel/index.html')

    if request.method == 'POST':
        filled_form = MerchantForms(request.POST)
        if filled_form.is_valid():
            note = "%s, your percel  is saved"%(filled_form.cleaned_data['name'])
            new_form = MerchantForms()
            return render(request, 'percel/index.html', {'merchantform':new_form, 'note':note})
    else:
        form = MerchantForms()
        return render(request, 'percel/index.html', {'merchantform':form})

