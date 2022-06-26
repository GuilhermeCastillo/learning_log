# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0005_topic'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
