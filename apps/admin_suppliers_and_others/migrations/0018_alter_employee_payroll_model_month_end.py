# Generated by Django 4.1.1 on 2022-11-01 07:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_suppliers_and_others', '0017_employee_payroll_model_net_salary_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_payroll_model',
            name='month_end',
            field=models.DateField(default=datetime.datetime(2022, 11, 1, 15, 0, 14, 28700), verbose_name='Choose Month End'),
        ),
    ]
