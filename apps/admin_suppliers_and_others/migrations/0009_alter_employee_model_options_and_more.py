# Generated by Django 4.1.1 on 2022-10-29 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_suppliers_and_others', '0008_employee_model_file_upload3_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee_model',
            options={'verbose_name': 'Employee', 'verbose_name_plural': 'Employees'},
        ),
        migrations.AlterModelOptions(
            name='supplier_model',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]
