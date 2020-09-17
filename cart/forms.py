from .models import ProductOrderItem
from django.forms import ModelForm

class ProductOrderItemForm(ModelForm):
    class Meta:
        model = ProductOrderItem
        fields = ['product','quantity','color']