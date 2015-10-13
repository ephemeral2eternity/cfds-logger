# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_leftclient'),
    ]

    operations = [
        migrations.CreateModel(
            name='link',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('src', models.CharField(max_length=20)),
                ('src_id', models.IntegerField()),
                ('dst', models.CharField(max_length=20)),
                ('dst_id', models.IntegerField()),
                ('link_type', models.IntegerField()),
                ('ts', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
