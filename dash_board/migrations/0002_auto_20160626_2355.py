# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dash_board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonAdapt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('ldsJobsReg', models.PositiveSmallIntegerField(verbose_name={'min_value': 0, 'max_value': 1}, null=True, blank=True)),
                ('completedMyPath', models.PositiveSmallIntegerField(verbose_name={'min_value': 0, 'max_value': 1}, null=True, blank=True)),
                ('selfRelianceGroup', models.TextField(null=True, blank=True)),
                ('education', models.TextField(null=True, blank=True)),
                ('lengthEducation', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('educationCompletion', models.DateField(null=True, blank=True)),
                ('employment', models.PositiveSmallIntegerField(verbose_name={'min_value': 0, 'max_value': 1}, null=True, blank=True)),
                ('newStart', models.PositiveSmallIntegerField(verbose_name={'min_value': 0, 'max_value': 2}, null=True, blank=True)),
                ('maritalStatus', models.PositiveSmallIntegerField(verbose_name={'min_value': 0, 'max_value': 1}, null=True, blank=True)),
                ('curchActivity', models.PositiveSmallIntegerField(verbose_name={'min_value': 0, 'max_value': 2}, null=True, blank=True)),
                ('placeResidence', models.PositiveSmallIntegerField(verbose_name={'min_value': 0, 'max_value': 1}, null=True, blank=True)),
                ('sixMonthPlan', models.TextField(null=True, blank=True)),
                ('contMissionProgress', models.PositiveSmallIntegerField(verbose_name={'min_value': 0, 'max_value': 6}, null=True, blank=True)),
                ('comments', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonBasic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('releaseDate', models.DateField()),
                ('name', models.TextField()),
                ('areaServingIng', models.TextField()),
                ('missionServinIn', models.TextField()),
                ('homeWardBranch', models.TextField()),
                ('homeStakeMiss', models.TextField()),
                ('homeArea', models.TextField()),
                ('homeCountry', models.TextField()),
                ('coordCouncil', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='admin',
            name='level',
            field=models.PositiveSmallIntegerField(verbose_name={'min_value': 1, 'max_value': 5}),
        ),
    ]
