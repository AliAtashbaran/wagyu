# Generated by Django 4.1.1 on 2022-11-04 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_comment_model_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment_model',
            name='email',
            field=models.EmailField(default='registered_user', max_length=100, verbose_name='Email'),
        ),
    ]
