import datetime
from django.utils.dateparse import parse_datetime
from django.contrib import messages
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
import dateutil.parser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.forms import inlineformset_factory, modelformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.views import View

from .models import *
from django.template import RequestContext as ctx
from .forms import *
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
    order = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    new = orders.filter(status='New').count()
    pending = orders.filter(status='Pending').count()
    context = {'orders': orders, 'customers': customers, 'pending': pending, 'new': new, 'order': order}
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
    # order
    customer = Customer.objects.get(id=pk)
    #order = Order(customer=customer, status="New")
    #order.save()
    order = Order.objects.get(id=171)

    orderform = OrderForm(instance=order)

    ##Task
    form = TaskForm(initial={'order': order})
    task = OrderTask.objects.filter(order=order)

    ##Services
    formservice = ServiceForm()
    service = ServiceItem.objects.filter(order=order)
    total=0
    for i in service:
        amount=i.price * i.quantity
        total=total+amount
    #files
    formfile=OrderFileForm()
    file=OrderFile.objects.filter(order=order)

    #info
    forminfo=infoForm()
    info=Orderinfo.objects.filter(order=order)

    # render
    context = {'info':info,'forminfo':forminfo,'total':total,'order': order, 'customer': customer, "form": form,
               "task": task, 'formservice': formservice, 'service': service, 'orderform': orderform,'formfile':formfile,'file':file}
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


def postOrder(request):

    temp=request.POST.get('date')
    date = dateutil.parser.parse(temp)
    id = request.POST.get('id')
    # request should be ajax and method should be POST.
    order = get_object_or_404(Order, id=id)
    form = OrderForm(instance=order)
    instance = form.save(commit=False)
    instance.date_finish = date
    instance.save()

    ser_instance = serializers.serialize('json', [instance, ])
    # send to client side.
    return JsonResponse({"instance": ser_instance}, status=200)


def postTask(request, id):
    # request should be ajax and method should be POST.
    if request.method == "POST":
        # get the form data
        form = TaskForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            order = get_object_or_404(Order, id=id)
            instance = form.save(commit=False)
            instance.order = order
            instance.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)



def upload_files(request,id):
    order = get_object_or_404(Order, id=id)
    files = [request.FILES.get('file')]
    for f in files:
        client_upload=OrderFile.objects.create(
            order=order,
            file=f,
        )
    return render(request,"accounts/order_form.html")



def order_info(request,id):
    print("here")
 # request should be ajax and method should be POST.
    if request.method == "POST":
        # get the form data
        form = infoForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            order = get_object_or_404(Order, id=id)
            instance = form.save(commit=False)
            instance.order = order
            instance.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)


def postService(request, id):
    # request should be ajax and method should be POST.
    if request.method == "POST":
        # get the form data
        form = ServiceForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            order = get_object_or_404(Order, id=id)
            instance = form.save(commit=False)
            instance.order = order
            instance.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [instance,])

            # send to client side.
            return JsonResponse({"instance": ser_instance,}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)


def deleteService(request):
    service = ServiceItem.objects.get(id=15)
    if request.method == "POST":
        service.delete()

    context = {'item': service}
    return render(request, 'accounts/delete.html', context)