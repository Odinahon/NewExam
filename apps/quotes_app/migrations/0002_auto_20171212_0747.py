# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-12 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='favorites',
            field=models.ManyToManyField(related_name='user_fav', to='login_reg.User'),
        ),
    ]