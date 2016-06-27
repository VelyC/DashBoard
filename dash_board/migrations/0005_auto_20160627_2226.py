# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dash_board', '0004_auto_20160627_2124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='missionarybasicmodel',
            name='missionServinIn',
        ),
        migrations.AddField(
            model_name='missionarybasicmodel',
            name='missionServingIn',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='missionarybasicmodel',
            name='areaServingIn',
            field=models.TextField(null=True, blank=True),
        ),
    ]
