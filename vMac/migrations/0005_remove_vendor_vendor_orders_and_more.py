# Generated by Django 4.2.7 on 2023-12-03 12:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vMac', '0004_vendor_vendor_orders_vendor_vendor_orders_completed_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='vendor_orders',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='vendor_orders_completed',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='vendor_orders_pending',
        ),
        migrations.AlterField(
            model_name='historicalperformance',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 3, 17, 49, 15, 370511)),
        ),
        migrations.AlterField(
            model_name='po',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 3, 17, 49, 15, 370511)),
        ),
    ]
