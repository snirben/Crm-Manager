from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import  inlineformset_factory
from .models import *
from .forms import OrderForm


# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    new = orders.filter(status='New').count()
    pending = orders.filter(status='Pending').count()
    context = {'orders': orders, 'customers': customers, 'pending': pending, 'new': new}
    return render(request, 'accounts/dashborad.html', context)


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})


def customer(request,pk):

    customer = Customer.objects.get(id=pk)
    orders= customer.order_set.all()
    orders_count=orders.count()
    context={'orders':orders,'customer':customer,'orders_count':orders_count}
    return render(request, 'accounts/customer.html',context)

def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Order,fields=('product','status'))
    customer = Customer.objects.get(id=pk)
    #form= OrderForm()
    formset= OrderFormSet(queryset=Order.objects.none(), instance=customer)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST,instance=customer)
        #form= OrderForm(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context={'formset':formset}
    return render(request,'accounts/order_form.html',context)

def UpdateOrder(request,pk):
    order=Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method=="POST":
        order.delete()
        return redirect('/')

    context={'item':order}
    return render(request,'accounts/delete.html',context)