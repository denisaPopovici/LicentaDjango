# Generated by Django 3.2 on 2022-04-21 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Licenta', '0023_alter_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
