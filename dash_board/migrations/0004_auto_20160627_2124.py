# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dash_board', '0003_auto_20160627_1829'),
    ]

    operations = [
        migrations.RenameField(
            model_name='missionarybasicmodel',
            old_name='areaServingIng',
            new_name='areaServingIn',
        ),
    ]
