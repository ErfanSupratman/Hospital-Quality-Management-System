# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 14:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdmInfo',
            fields=[
                ('AdmInfo_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('dt', models.DateTimeField(verbose_name='date published')),
                ('name', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=4)),
                ('memCode', models.CharField(max_length=15)),
                ('prCode', models.IntegerField(default=0)),
                ('isAdmEr', models.BooleanField(default=False)),
                ('isAdmEe', models.BooleanField(default=False)),
                ('isOnUse', models.BooleanField(default=False)),
                ('isDeleted', models.BooleanField(default=False)),
                ('isCmted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AgentInfo',
            fields=[
                ('AgentInfo_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('dt', models.DateTimeField(verbose_name='date published')),
                ('name', models.CharField(max_length=10)),
                ('code', models.CharField(max_length=5)),
                ('memCode', models.CharField(max_length=5)),
                ('isOnUse', models.BooleanField(default=False)),
                ('isOp', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CheInfo',
            fields=[
                ('CheInfo_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('dt', models.DateTimeField(verbose_name='date published')),
                ('time', models.DateField(verbose_name='date published')),
                ('categroy', models.CharField(max_length=50)),
                ('manageScore', models.IntegerField(default=0)),
                ('personScore', models.IntegerField(default=0)),
                ('fee', models.IntegerField(default=0)),
                ('reason', models.TextField()),
                ('fk_CheInfo_admEeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CheInfo_admEeId', to='main.AdmInfo')),
                ('fk_CheInfo_admErId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CheInfo_admErId', to='main.AdmInfo')),
                ('fk_CheInfo_opId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CheInfo_opId', to='main.AgentInfo')),
            ],
        ),
        migrations.AddField(
            model_name='adminfo',
            name='fk_AdmInfo_opId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AdmInfo_opId', to='main.AgentInfo'),
        ),
    ]
