from django.contrib import messages
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory, modelformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.views import View

from .models import *
from .forms import OrderForm, CreateUserForm, ProductForm, OrderItemForm, CustomerForm,TaskForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
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


def indexView(request):
    form = CustomerForm()
    customer = Customer.objects.all()
    return render(request, "accounts/customer.html", {"form": form, "customer": customer})


def postCustomer(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = CustomerForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


def checkCustomerName(request):
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        name = request.GET.get("name", None)
        # check for the nick name in the database.
        if Customer.objects.filter(name=name).exists():
            # if nick_name found return not valid new friend
            return JsonResponse({"valid": False}, status=200)
        else:
            # if nick_name not found, then user can create a new friend.
            return JsonResponse({"valid": True}, status=200)

    return JsonResponse({}, status=400)





















@login_required(login_url="login")
def createOrder(request, pk):
    customer = Customer.objects.get(id=pk)
    order = Order(customer=customer, status="New")
    order.save()
    formset = OrderItemForm(initial={'order': order})
    form = TaskForm(initial={'order': order})
    task = OrderTask.objects.filter(order=order)
    if request.method == 'POST':
        formset = OrderItemForm(request.POST)
        if formset.is_valid():
            formset.save()

    context = {'formset': formset, 'order': order, 'customer': customer,"form": form, "task": task}
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


def postTask(request,id):
    # request should be ajax and method should be POST.
    if request.method == "POST":
        # get the form data
        form = TaskForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            order = get_object_or_404(Order, id=id)
            instance = form.save(commit=False)
            instance.order=order
            instance.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

