from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Stock
from .forms import StockCreateForm, StockSearchForm, StockUpdateForm
# Create your views here.


def index(request):
    title = "Welcome This Is Home Page"
    context = {
        "title": title,
    }
    return render(request, 'dashboard/index.html', context)


def list_item(request):
    title = "List Item"
    form = StockSearchForm(request.POST or None)
    queryset = Stock.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
        "form": form,
    }
    if request.method == 'POST':
        queryset = Stock.objects.filter(
            catagory__icontains=form['catagory'].value(),
            item_name__icontains=form['item_name'].value()
        )
        context = {
            "form": form,
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


def update_item(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/list_item')

    context = {
        "form": form
    }

    return render(request, 'dashboard/add_item.html', context)


def delete_item(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)
    if request.method == "POST":
        queryset.delete()
        return redirect("/list_item")
    return render(request, "dashboard/confirm_delete.html")
