from django import forms
from .models import Destination, Merchant, Product

class MerchantForms(forms.ModelForm):
    class Meta:
        model = Merchant
        fields = '__all__'
        labels = {'name':'Merchant\'s name', 'products':'Products to deliver', 'total_weight':'Total Weight', 'destinations': 'Parcel destination'}
        widgets = {
            'products': forms.Textarea(attrs={'cols': 50, 'rows': 2}),
        }
        


class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {'percel_id':'Parcel Id', 'product_type':'Product Types'}
        