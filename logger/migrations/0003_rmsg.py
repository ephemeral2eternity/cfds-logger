# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0002_msg_qoe'),
    ]

    operations = [
        migrations.CreateModel(
            name='rMSG',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('client', models.CharField(max_length=20)),
                ('faulty_node', models.CharField(max_length=20)),
                ('recovery_node', models.CharField(max_length=20)),
                ('recovery_peer', models.CharField(max_length=20)),
                ('qoe', models.DecimalField(max_digits=6, default=-1.0, decimal_places=4)),
                ('recovery_qoe', models.DecimalField(max_digits=6, default=-1.0, decimal_places=4)),
                ('video', models.IntegerField()),
                ('recovery_time', models.DecimalField(max_digits=6, default=-1.0, decimal_places=4)),
                ('msg', models.CharField(max_length=200)),
                ('msg_type', models.IntegerField()),
                ('ts', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
