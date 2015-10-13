# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='msg',
            name='qoe',
            field=models.DecimalField(max_digits=6, decimal_places=4, default=-1.0),
        ),
    ]
