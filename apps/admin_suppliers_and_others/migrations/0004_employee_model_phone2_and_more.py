# Generated by Django 4.1.1 on 2022-10-28 13:39

import apps.admin_suppliers_and_others.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_suppliers_and_others', '0003_employee_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_model',
            name='phone2',
            field=models.CharField(max_length=15, null=True, verbose_name='2nd Phone'),
        ),
        migrations.AlterField(
            model_name='employee_model',
            name='file_upload',
            field=models.FileField(default='no documents available', upload_to=apps.admin_suppliers_and_others.models.emp_upload_file, verbose_name='other documents'),
        ),
        migrations.AlterField(
            model_name='employee_model',
            name='phone',
            field=models.CharField(max_length=15, null=True, verbose_name='Phone'),
        ),
    ]