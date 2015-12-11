# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skool', '0004_auto_20151202_0929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='user',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
    ]
