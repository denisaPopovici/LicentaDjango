# Generated by Django 3.2 on 2022-03-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Licenta', '0011_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(),
        ),
    ]
