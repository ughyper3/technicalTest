from django.forms import ModelForm
from .models import Product

# class productForm extends ModelForm abstract class generate automatically a form

class productForm(ModelForm):
    class Meta:
        model = Product
        fields = ['GTIN', 'name', 'price', 'expiryDate']

