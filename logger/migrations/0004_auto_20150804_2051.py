# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0003_rmsg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rmsg',
            name='recovery_time',
            field=models.DecimalField(max_digits=6, decimal_places=4),
        ),
    ]
