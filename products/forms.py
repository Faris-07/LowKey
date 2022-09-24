from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        names_to_display = [(c.id, c.get_name_to_display()) for c in categories]

        self.fields['category'].choices = names_to_display
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black text-dark rounded-0'
