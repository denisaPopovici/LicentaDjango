# Generated by Django 3.2.7 on 2021-11-15 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Licenta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='image',
            field=models.CharField(default='', max_length=200),
        ),
    ]
