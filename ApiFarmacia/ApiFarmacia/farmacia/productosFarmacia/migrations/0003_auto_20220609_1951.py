# Generated by Django 3.2.3 on 2022-06-09 23:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productosFarmacia', '0002_auto_20220609_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='id_producto',
            field=models.IntegerField(default=1, primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='productos',
            name='stock_producto',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)]),
        ),
    ]
