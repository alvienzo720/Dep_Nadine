# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-08 23:01


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nadine', '0008_add_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailylog',
            name='member',
        ),
        migrations.RemoveField(
            model_name='membernote',
            name='member',
        ),
        migrations.RemoveField(
            model_name='securitydeposit',
            name='member',
        ),
        migrations.RemoveField(
            model_name='sentemaillog',
            name='member',
        ),
        migrations.RemoveField(
            model_name='specialday',
            name='member',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='member',
        ),
        migrations.AlterField(
            model_name='dailylog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique_for_date='visit_date'),
        ),
    ]
