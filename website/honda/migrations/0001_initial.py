# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('race', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=25, default='Pop', choices=[('Matic', 'Matic'), ('Cub', 'Cub'), ('Sport', 'Sport'), ('BigBike', 'BigBike')])),
                ('color', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]
