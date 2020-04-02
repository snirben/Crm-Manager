# Generated by Django 3.0.4 on 2020-04-01 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0033_auto_20200401_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderfile',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Order'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Order'),
        ),
        migrations.AlterField(
            model_name='ordertask',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Order'),
        ),
        migrations.AlterField(
            model_name='serviceitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Order', verbose_name='הזמנה'),
        ),
    ]
