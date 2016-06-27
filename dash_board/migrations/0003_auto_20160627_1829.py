# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dash_board', '0002_auto_20160626_2355'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminModel',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('level', models.PositiveSmallIntegerField(verbose_name={'min_value': 1, 'max_value': 5})),
                ('home_location', models.TextField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='PersonAdapt',
            new_name='MissionaryAdaptationModel',
        ),
        migrations.RenameModel(
            old_name='PersonBasic',
            new_name='MissionaryBasicModel',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='author',
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
    ]
