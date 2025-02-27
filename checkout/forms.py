from django import forms
from .models import ShippingInfo


class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingInfo
        exclude = ('user',)
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'state',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name*',
            'email': 'Email Address*',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code*',
            'town_or_city': 'Town or City*',
            'street_address1': 'Street Address 1*',
            'street_address2': 'Street Address 2',
            'state': 'County, State or Locality*',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].label = False
            if field != 'street_address2':
                if field != 'phone_number':
                    self.fields[field].widget.attrs['required'] = True
            if field != 'country':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
