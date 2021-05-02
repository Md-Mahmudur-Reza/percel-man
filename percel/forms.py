from django import forms
from .models import Destination, Merchant

class MerchantForms(forms.ModelForm):
    class Meta:
        model = Merchant
        fields = ['merchant_id', 'name', 'products', 'total_weight', 'destinations']

