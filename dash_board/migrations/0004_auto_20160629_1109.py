# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dash_board', '0003_auto_20160629_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missionaryadaptationmodel',
            name='churchActivity',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='missionaryadaptationmodel',
            name='comments',
            field=models.TextField(default='comment here ~'),
        ),
        migrations.AlterField(
            model_name='missionaryadaptationmodel',
            name='completedMyPath',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='missionaryadaptationmodel',
            name='contMissionProgress',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='missionaryadaptationmodel',
            name='education',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='missionaryadaptationmodel',
            name='educationCompletion',
            field=models.DateField(default='1900-01-01'),
        ),
        migrations.AlterField(
            model_name='missionaryadaptationmodel',
            name='employment',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='missionaryadaptationmodel',
            name='ldsJobsReg',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='missionaryadaptationmodel',
            name='lengthEducation',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='missionaryadaptationmodel',
            name='maritalStatus',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='missionaryadaptationmodel',
            name='newStart',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='missionaryadaptationmodel',
            name='placeResidence',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='missionaryadaptationmodel',
            name='selfRelianceGroup',
            field=models.TextField(default=''),
        ),
    ]
