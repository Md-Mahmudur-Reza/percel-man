from django import forms
from .models import Destination, Merchant

class MerchantForms(forms.ModelForm):
    # destination = forms.ModelChoiceField(queryset=Destination.objects, empty_label=None, label='Percel destination')
    class Meta:
        model = Merchant
        fields = '__all__'
        labels = {'name':'Name', 'products':'Products to deliver', 'total_weight':'Total Weight', 'destinations': 'Percel destination'}
        widgets = {
            'products': forms.Textarea(attrs={'cols': 50, 'rows': 2}),
        }
        

