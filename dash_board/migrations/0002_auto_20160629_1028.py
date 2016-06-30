# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dash_board', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='missionaryadaptationmodel',
            old_name='curchActivity',
            new_name='churchActivity',
        ),
    ]
