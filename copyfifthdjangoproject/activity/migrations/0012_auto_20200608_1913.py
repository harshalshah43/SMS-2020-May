# Generated by Django 3.0.4 on 2020-06-08 13:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0011_auto_20200607_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='expires_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 9, 13, 43, 3, 717192, tzinfo=utc)),
        ),
    ]
