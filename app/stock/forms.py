from django import forms
from .models import Stock


class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['catagory', 'item_name', 'quantity']
