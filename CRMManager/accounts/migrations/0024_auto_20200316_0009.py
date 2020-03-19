# Generated by Django 3.0.3 on 2020-03-15 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20200314_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='static/files/')),
            ],
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
