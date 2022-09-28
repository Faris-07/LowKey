from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """ form for users to place order """
    class Meta:
        """ Gets chosen fields from Order model """
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2', 'town_city',
                  'county', 'postcode', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full name',
            'email': 'Email',
            'phone_number': 'Phone number',
            'postcode': 'Post code',
            'town_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'country': 'Country',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
