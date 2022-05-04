# Generated by Django 3.2 on 2022-04-25 21:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Licenta', '0025_auto_20220424_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inferior_limit', models.IntegerField(default=0)),
                ('superior_limit', models.IntegerField(default=0)),
                ('name', models.CharField(default='One', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.date(2022, 4, 25)),
        ),
    ]
