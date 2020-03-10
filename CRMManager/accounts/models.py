from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

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
    price = models.FloatField(verbose_name='מחיר', null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY, verbose_name='קטגוריה')
    description = models.CharField(max_length=200, null=True, verbose_name='מלל חופשי')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True,verbose_name="כמות")

    def __str__(self):
        return self.product.name



class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Work in progress', 'Work in progress'),
        ('completed', 'completed'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    #  def __str__(self):
    #     return self.id

    def date_createdview(self):
        return self.date_created.strftime('%d/%m/%Y')

class OrderItem(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return self.product.name
