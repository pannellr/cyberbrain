# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leaf',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('mac_address', models.CharField(max_length=200)),
                ('last_seen_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
