# Generated by Django 4.1.1 on 2022-10-26 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_model_view_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_model',
            name='order_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]