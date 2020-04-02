from locale import str

from django.db import models


# Create your models here.

class Customer(models.Model):
    #name will be unique
    name = models.CharField(verbose_name='שם מלא',max_length=200, null=True)
    company = models.CharField(verbose_name='חברה',max_length=200, null=True)
    phone = models.CharField(verbose_name='סלולרי',max_length=200, null=True)
    email = models.CharField(verbose_name='אימייל',max_length=200, null=True)
    address = models.CharField(verbose_name='כתובת',max_length=200, null=True)
    date_created = models.DateTimeField(verbose_name='תאריך יצירה',auto_now_add=True)

    def __str__(self):
        return self.name

    def date_createdview(self):
        return self.date_created.strftime('%B %d %Y')


class Product(models.Model):
    CATEGORY = (
        ('General', 'General'),
        ('SmartHome', 'SmartHome'),
        ('Software', 'Software'),
        ('Mobile', 'Mobile'),

    )
    name = models.CharField(verbose_name='שם', max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY, verbose_name='קטגוריה')
    description = models.CharField(max_length=200, null=True, verbose_name='מלל חופשי')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('New', 'חדש'),
        ('Work in progress', 'Work in progress'),
        ('completed', 'completed'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_finish = models.DateField(null=True, verbose_name='תאריך סיום' ,blank=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS, verbose_name='סטאטוס')
    desc = models.TextField(max_length=255, null=True, verbose_name='פרטים',blank=True)
    paid = models.BooleanField(default=False)
    def date_createdview(self):
        return self.date_created.strftime('%d/%m/%Y')

    def __str__(self):
        return str(self.id)


class ServiceItem(models.Model):
    service = models.CharField(max_length=255,null=True,verbose_name='שרות')
    order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE,verbose_name='הזמנה')
    quantity = models.IntegerField(null=True,verbose_name='כמות')
    price = models.FloatField(verbose_name='מחיר', null=True)

    def amount(self):
       return self.price * self.quantity
# def __str__(self):
#    return self.product.name

class OrderTask(models.Model):
    order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    task = models.CharField(max_length=200, null=True, verbose_name='משימה')

class OrderFile(models.Model):
    order=models.ForeignKey(Order, null=True, on_delete=models.CASCADE)
    file= models.FileField(upload_to='static/files/')
    uploaded_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
     return self.file.name
    def date_created(self):
        return self.uploaded_at.strftime('%d/%m/%Y')


class Orderinfo(models.Model):
      order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE)
      created_at = models.DateTimeField(auto_now_add=True, null=True)
      desc = models.TextField(max_length=255, null=True, verbose_name='פרטים', blank=True)