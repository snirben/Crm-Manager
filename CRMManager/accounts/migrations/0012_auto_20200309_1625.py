# Generated by Django 3.0.3 on 2020-03-09 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20200308_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Order'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('General', 'General'), ('SmartHome', 'SmartHome'), ('Software', 'Software'), ('Mobile', 'Mobile')], max_length=200, null=True, verbose_name='קטגוריה'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=200, null=True, verbose_name='מלל חופשי'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='שם'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True, verbose_name='מחיר'),
        ),
    ]
