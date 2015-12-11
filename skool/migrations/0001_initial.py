# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('code', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('emp_id', models.PositiveIntegerField(db_index=True)),
                ('name', models.CharField(max_length=64)),
                ('mobile_no', models.CharField(max_length=10, db_index=True)),
                ('qualification', models.CharField(max_length=5)),
                ('email', models.EmailField(max_length=254)),
                ('DOJ', models.DateField()),
                ('DOB', models.DateField()),
                ('salary', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roll_no', models.PositiveIntegerField(db_index=True)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=32)),
                ('state', models.CharField(max_length=32)),
                ('standard', models.CharField(max_length=32)),
                ('sem', models.PositiveIntegerField()),
                ('DOA', models.DateField()),
                ('DOB', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=10, db_index=True)),
                ('department', models.ForeignKey(related_name='department', to='skool.Department')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='HOD',
            field=models.ForeignKey(related_name='hod', to='skool.Faculty'),
        ),
    ]
