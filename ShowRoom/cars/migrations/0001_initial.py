# Generated by Django 5.1.3 on 2024-11-22 19:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hex_code', models.CharField(help_text='Hexadecimal color code (e.g., #FFFFFF)', max_length=7)),
                ('rgb_value', models.CharField(help_text='RGB value (e.g., rgb(255, 255, 255))', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='cars/photos/')),
                ('specs', models.TextField()),
                ('model', models.CharField(max_length=50)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='brands.brand')),
                ('colors', models.ManyToManyField(related_name='cars', to='cars.color')),
            ],
        ),
    ]