# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-23 22:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_auto_20170523_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaddetalle',
            name='etapa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='lead_etapa', to='crm.EtapasLeads'),
        ),
    ]