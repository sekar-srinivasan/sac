# Generated by Django 2.1.1 on 2018-10-10 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('contact_name', models.CharField(max_length=250)),
                ('contact_phone', models.CharField(blank=True, max_length=20)),
                ('contact_email', models.EmailField(blank=True, max_length=100)),
                ('contact_addr_street', models.CharField(blank=True, max_length=250)),
                ('contact_addr_apt', models.CharField(blank=True, max_length=10)),
                ('contact_addr_city', models.CharField(blank=True, max_length=50)),
                ('contact_addr_state', models.CharField(blank=True, max_length=100)),
                ('contact_addr_zip', models.CharField(blank=True, max_length=6)),
                ('location_addr_street', models.CharField(blank=True, max_length=250)),
                ('location_addr_apt', models.CharField(blank=True, max_length=10)),
                ('location_addr_city', models.CharField(blank=True, max_length=50)),
                ('location_addr_state', models.CharField(blank=True, max_length=100)),
                ('location_addr_zip', models.CharField(blank=True, max_length=6)),
                ('project_partner_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
