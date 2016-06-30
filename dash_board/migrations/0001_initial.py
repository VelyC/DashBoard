# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminModel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('level', models.PositiveSmallIntegerField()),
                ('home_location', models.TextField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MissionaryAdaptationModel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('ldsJobsReg', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('completedMyPath', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('selfRelianceGroup', models.TextField(blank=True, null=True)),
                ('education', models.TextField(blank=True, null=True)),
                ('lengthEducation', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('educationCompletion', models.DateField(blank=True, null=True)),
                ('employment', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('newStart', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('maritalStatus', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('curchActivity', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('placeResidence', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('sixMonthPlan', models.TextField(blank=True, null=True)),
                ('contMissionProgress', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MissionaryBasicModel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('releaseDate', models.DateField()),
                ('name', models.TextField()),
                ('areaServingIn', models.TextField(blank=True, null=True)),
                ('missionServingIn', models.TextField(blank=True, null=True)),
                ('homeWardBranch', models.TextField()),
                ('homeStakeMiss', models.TextField()),
                ('homeArea', models.TextField()),
                ('homeCountry', models.TextField()),
                ('coordCouncil', models.TextField()),
            ],
        ),
    ]
