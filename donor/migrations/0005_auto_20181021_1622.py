# Generated by Django 2.1.1 on 2018-10-21 16:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0004_auto_20181021_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2019, 10, 21, 16, 22, 49, 684510, tzinfo=utc)),
        ),
    ]