# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-27 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_teacher_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='tags',
            field=models.CharField(default='', max_length=10, verbose_name='Course tag'),
        ),
    ]