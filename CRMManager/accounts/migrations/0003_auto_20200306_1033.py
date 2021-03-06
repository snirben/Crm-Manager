# Generated by Django 3.0.3 on 2020-03-06 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_order_proudct'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Proudct',
            new_name='Product',
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for Delivery', 'Out for Delivery'), ('Deliverd', 'Deliverd')], max_length=200, null=True),
        ),
    ]
