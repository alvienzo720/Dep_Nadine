# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 21:15


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nadine', '0022_organization_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='blurb',
            field=models.CharField(blank=True, max_length=112, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]