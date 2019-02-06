# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-02-06 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0140_auto_20190206_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='employmenttimecommitment',
            name='job_description',
            field=models.TextField(default='not provided', help_text='Please tell us about the work you do and your job duties.', max_length=3000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employmenttimecommitment',
            name='job_title',
            field=models.TextField(default='unknown', max_length=100),
            preserve_default=False,
        ),
    ]
