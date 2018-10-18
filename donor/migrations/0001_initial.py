# Generated by Django 2.1.1 on 2018-10-10 20:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('child', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsorship_amount', models.FloatField()),
                ('expiry_date', models.DateField(default=datetime.date(2019, 10, 10))),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='donation_children', to='child.Child')),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('addr_street', models.CharField(blank=True, max_length=250)),
                ('addr_apt', models.CharField(blank=True, max_length=10)),
                ('addr_city', models.CharField(blank=True, max_length=50)),
                ('addr_state', models.CharField(blank=True, max_length=100)),
                ('addr_zip', models.CharField(blank=True, max_length=6)),
                ('active', models.BooleanField(default=True)),
                ('donor_user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='donation',
            name='donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='donation_donors', to='donor.Donor'),
        ),
    ]
