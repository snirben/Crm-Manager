from builtins import super

from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CustomerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
            model = Customer
            fields = "__all__"

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class OrderItemForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['quantity','product','order']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
class TaskForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for task in self.fields.keys():
            self.fields[task].widget.attrs.update({
                'class': 'form-control',
            })
        self.fields['order'].required = False
    class Meta:
        model= OrderTask
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
