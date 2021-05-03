from django import forms
from .models import Destination, Merchant, Product

class MerchantForms(forms.ModelForm):
    # destination = forms.ModelChoiceField(queryset=Destination.objects, empty_label=None, label='Percel destination')
    class Meta:
        model = Merchant
        fields = '__all__'
        labels = {'name':'Name', 'products':'Products to deliver', 'total_weight':'Total Weight', 'destinations': 'Percel destination'}
        widgets = {
            'products': forms.Textarea(attrs={'cols': 50, 'rows': 2}),
        }
        


class ProductForms(forms.ModelForm):
    # product_type = forms.ChoiceField(choices=ProductTypeChoice, label= 'Product Types')
    # product_type = forms.ModelChoiceField(queryset=Product.objects.all(), empty_label=None, label='Types of products')
    # percel_id = forms.ModelChoiceField(queryset=Merchant.objects.get('name'),empty_label=None, label='Merchant')
    class Meta:
        model = Product
        fields = '__all__'
        labels = {'percel_id':'Percel Id', 'product_type':'Product Types'}
        