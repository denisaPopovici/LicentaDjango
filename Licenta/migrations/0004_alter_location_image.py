# Generated by Django 3.2 on 2021-12-02 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Licenta', '0003_alter_location_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]