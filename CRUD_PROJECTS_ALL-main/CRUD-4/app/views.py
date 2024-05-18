from django.shortcuts import render,redirect
from .forms import OrderForm
from .models import Order
# Create your views here.
def home(request):
    return render(request, 'home.html')

def order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                return redirect('/show')
        except :
            pass
    else:
        form = OrderForm()
    return render(request, 'index.html',{'form':form})
        
def show(request):
    orders = Order.objects.order_by('name')
    return render(request, 'show.html',{"orders":orders})

def edit(request, oid):
    order  = Order.objects.get(oid=oid)
    return render(request, 'edit.html',{"order":order})

def update(request, oid):
    order  = Order.objects.get(oid=oid)
    form = OrderForm(request.POST, instance=order)
    if form.is_valid():
            form.save()
            return redirect('/show')
    return render(request, 'edit.html',{"order":order})

def delete(request, oid):
    order = Order.objects.get(oid=oid)
    order.delete()
    return redirect('/show')