# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151030_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='visability',
            field=models.IntegerField(default=0, choices=[(0, b'Public'), (1, b'Anonymous')]),
        ),
        migrations.AddField(
            model_name='review',
            name='visability',
            field=models.IntegerField(default=0, choices=[(0, b'Public'), (1, b'Anonymous')]),
        ),
    ]
