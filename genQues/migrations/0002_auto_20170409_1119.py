# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-09 05:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genQues', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rankingset',
            options={'ordering': ['-userScore', 'correctans']},
        ),
    ]