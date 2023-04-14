# Generated by Django 3.2 on 2023-03-26 17:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0004_alter_transactions_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='email',
            field=models.EmailField(default='h1337328@gmail.com', max_length=50),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='Date_Time',
            field=models.CharField(default=datetime.datetime(2023, 3, 26, 17, 19, 41, 281456, tzinfo=utc), max_length=19),
        ),
    ]