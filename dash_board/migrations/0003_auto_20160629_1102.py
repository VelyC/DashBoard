# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dash_board', '0002_auto_20160629_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missionaryadaptationmodel',
            name='ldsJobsReg',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
