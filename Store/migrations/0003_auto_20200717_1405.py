# Generated by Django 3.0.4 on 2020-07-17 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_auto_20200717_1404'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='custome',
            new_name='customer',
        ),
    ]
