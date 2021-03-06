# Generated by Django 3.0.4 on 2020-07-17 08:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(blank=True, default='', max_length=280, null=True)),
                ('image', models.ImageField(upload_to='uploads/products/')),
                ('category', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='Store.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField(default=0)),
                ('address', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('phone', models.CharField(blank=True, default='', max_length=13, null=True)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.Customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.Product')),
            ],
        ),
    ]
