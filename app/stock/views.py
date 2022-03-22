from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Stock
from .forms import StockCreateForm
# Create your views here.


def index(request):
    title = "Welcome This Is Home Page"
    context = {
        "title": title,
    }
    return render(request, 'dashboard/index.html', context)


def list_item(request):
    title = "List Item"
    queryset = Stock.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "dashboard/list_item.html", context)


def add_item(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list_item')
    context = {
        "form": form,
        "title": "Add Item",
    }
    return render(request, "dashboard/add_item.html", context)
