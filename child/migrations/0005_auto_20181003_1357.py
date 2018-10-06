# Generated by Django 2.1.1 on 2018-10-03 13:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0004_auto_20180921_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='project_partner_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project_children', to=settings.AUTH_USER_MODEL),
        ),
    ]