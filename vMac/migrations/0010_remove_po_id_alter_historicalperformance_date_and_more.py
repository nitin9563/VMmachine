# Generated by Django 4.2.7 on 2023-12-04 18:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vMac', '0009_alter_historicalperformance_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='po',
            name='id',
        ),
        migrations.AlterField(
            model_name='historicalperformance',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 4, 23, 58, 39, 560127)),
        ),
        migrations.AlterField(
            model_name='po',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 4, 23, 58, 39, 560127)),
        ),
        migrations.AlterField(
            model_name='po',
            name='po_number',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]
