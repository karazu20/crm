# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-29 17:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0021_auto_20170529_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaddetalle',
            name='ejecutivo_principal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ejecutivo_prin_lead', to='crm.EjecutivoComercial'),
        ),
    ]