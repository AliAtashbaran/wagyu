# Generated by Django 4.1.1 on 2022-10-24 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('category', models.CharField(choices=[('acc', 'Account'), ('sup', 'Supply'), ('prd', 'Products'), ('web', 'Website_issue'), ('ord', 'Order'), ('pay', 'Payment')], max_length=20)),
                ('description', models.TextField()),
                ('registered', models.DateTimeField(auto_now_add=True)),
                ('user_register', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
