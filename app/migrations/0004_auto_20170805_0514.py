# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-05 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_demo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=30, null=True, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='mid_name',
            field=models.CharField(max_length=30, null=True, verbose_name='Middle name'),
        ),
    ]
