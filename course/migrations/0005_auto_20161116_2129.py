# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-16 12:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_enroll'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='enroll',
            unique_together=set([('sid', 'courseno')]),
        ),
    ]
