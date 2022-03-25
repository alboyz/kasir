from django import forms
from .models import Stock


class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['catagory', 'item_name', 'quantity']

    def clean_catagory(self):
        catagory = self.cleaned_data.get('catagory')
        if not catagory:
            raise forms.ValidationError('Tidak boleh kosong')

        for instance in Stock.objects.all():
            if instance.catagory == catagory:
                raise forms.ValidationError(catagory + ' ' + 'sudah digunakan')
        return catagory

    def clean_item_name(self):
        item_name = self.cleaned_data.get('item_name')
        if not item_name:
            raise forms.ValidationError('Tidak boleh kosong')
        return item_name


class StockSearchForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['catagory', 'item_name']


class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['catagory', 'item_name', 'quantity']
