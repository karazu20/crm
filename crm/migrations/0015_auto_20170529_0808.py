# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-29 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0014_auto_20170526_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaddetalle',
            name='causa_salida',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
