from django.contrib import admin
from .models import Stock
from .forms import StockCreateForm


class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['catagory', 'item_name', 'quantity']
    form = StockCreateForm
    list_filter = ['catagory']
    search_fields = ['catagory', 'list_item']


admin.site.register(Stock, StockCreateAdmin)
