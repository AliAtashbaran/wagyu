# Generated by Django 4.1.1 on 2022-11-03 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_suppliers_and_others', '0019_alter_employee_payroll_model_month_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_payroll_model',
            name='month_end',
            field=models.DateField(default=datetime.datetime(2022, 11, 3, 18, 35, 58, 494285), verbose_name='Choose Month End'),
        ),
    ]