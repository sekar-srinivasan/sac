# Generated by Django 2.1.1 on 2018-11-06 02:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('age', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, default='child_pics/happy_apna_skool_kid.jpg', upload_to='child_pics')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_children', to='project.Project')),
                ('project_partner_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='partner_user_children', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress_date', models.DateField(default=django.utils.timezone.now)),
                ('milestone', models.CharField(blank=True, max_length=100)),
                ('short_description', models.CharField(max_length=250)),
                ('long_description', models.TextField(blank=True)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='child.Child')),
            ],
        ),
    ]
