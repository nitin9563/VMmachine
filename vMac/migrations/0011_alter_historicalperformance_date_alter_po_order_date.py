# Generated by Django 4.2.7 on 2023-12-04 18:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vMac', '0010_remove_po_id_alter_historicalperformance_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalperformance',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 5, 0, 22, 0, 118614)),
        ),
        migrations.AlterField(
            model_name='po',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 5, 0, 22, 0, 118614)),
        ),
    ]
