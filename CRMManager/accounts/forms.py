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

class ServiceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        for service in self.fields.keys():
            self.fields[service].widget.attrs.update({
                'class': 'form-control',
            })
        self.fields['order'].required = False
    class Meta:
        model= ServiceItem
        fields = '__all__'

class DateInput(forms.DateInput):
    input_type= 'date'


class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['date_finish'].required = False
        self.fields['status'].required = False
        self.fields['desc'].required = False

    class Meta:
        model = Order
        fields = '__all__'
        widgets = {'date_finish': DateInput(),}






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


class OrderFileForm(ModelForm):
    class Meta:
        model=OrderFile
        fields='__all__'
