# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-08 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20170408_0650'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstat',
            name='TotalCorrectAns',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='userstat',
            name='TotalWrongAns',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='userstat',
            name='NumGamePlayed',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
