from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory, modelformset_factory
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import OrderForm, CreateUserForm, ProductForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout


# Create your views here.

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    products = Product.objects.all()
    context = {'form': form, 'products': products}
    return render(request, 'accounts/products.html', context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username Or Password Is Incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url="login")
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    new = orders.filter(status='New').count()
    pending = orders.filter(status='Pending').count()
    context = {'orders': orders, 'customers': customers, 'pending': pending, 'new': new, }
    return render(request, 'accounts/dashborad.html', context)


@login_required(login_url="login")
def products(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    products = Product.objects.all()
    context = {'form': form, 'products': products}
    return render(request, 'accounts/products.html', context)


@login_required(login_url="login")
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_count = orders.count()
    context = {'orders': orders, 'customer': customer, 'orders_count': orders_count}
    return render(request, 'accounts/customer.html', context)


@login_required(login_url="login")
def createOrder(request, pk):
    customer = Customer.objects.get(id=pk)
    neworder=Order(customer=customer,status="New")
    neworder.save()
    formset1 = modelformset_factory(OrderItem,fields=("quantity","product",), extra=1)
    formset = formset1(queryset=OrderItem.objects.none(),)
    context = {'formset':  formset,'products':products}
    return render(request, 'accounts/order_form.html', context)


@login_required(login_url="login")
def UpdateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


@login_required(login_url="login")
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'accounts/delete.html', context)


def item_list(request):
    context = {
        ''
    }
    return render(request, "item_list".html, context)


def add_to_order(request):
    item = get_object_or_404(products)
    order_item = OrderItem.objects.create(item=item)
    order = Order.objects.create(user=request.user)
    order.items.add(order_item)
    return redirect(request, '')
