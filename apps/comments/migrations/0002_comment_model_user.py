# Generated by Django 4.1.1 on 2022-11-04 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment_model',
            name='user',
            field=models.CharField(default='empty', max_length=30, verbose_name='User'),
            preserve_default=False,
        ),
    ]
