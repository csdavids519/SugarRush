from django import forms
from .models import Orders


class OrderForm(forms.ModelForm):
    phone_number = forms.CharField(required=False)
    street_address2 = forms.CharField(required=False)
    postcode = forms.CharField(required=True)

    class Meta:
        model = Orders
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'state',)
