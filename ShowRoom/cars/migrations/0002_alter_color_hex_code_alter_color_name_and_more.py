# Generated by Django 5.1.3 on 2024-11-22 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='hex_code',
            field=models.CharField(blank=True, max_length=7),
        ),
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(choices=[('Black', 'Black'), ('White', 'White'), ('Red', 'Red'), ('Blue', 'Blue')], default='Black', max_length=20),
        ),
        migrations.AlterField(
            model_name='color',
            name='rgb_value',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
