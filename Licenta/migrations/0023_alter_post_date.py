# Generated by Django 3.2 on 2022-04-21 12:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Licenta', '0022_remove_visitedlocations_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.date(2022, 4, 21)),
        ),
    ]
