# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='msg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('client', models.CharField(max_length=20)),
                ('node', models.CharField(max_length=20)),
                ('video', models.IntegerField()),
                ('msg', models.CharField(max_length=200)),
                ('msg_type', models.IntegerField()),
                ('ts', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
