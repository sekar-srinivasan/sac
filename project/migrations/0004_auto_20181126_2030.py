# Generated by Django 2.1.1 on 2018-11-26 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_project_sponsorship_amount_per_child'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='sponsorship_amount_per_child',
            new_name='sponsorship_needed_per_child',
        ),
    ]
