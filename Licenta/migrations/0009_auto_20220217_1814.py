# Generated by Django 3.2 on 2022-02-17 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Licenta', '0008_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Licenta.location'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Licenta.customuser'),
        ),
    ]