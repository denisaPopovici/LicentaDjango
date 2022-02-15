# Generated by Django 3.2.7 on 2021-11-15 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Location', max_length=100)),
                ('latitude', models.CharField(default='', max_length=12)),
                ('longitude', models.CharField(default='', max_length=13)),
                ('image', models.FileField(blank=True, default='', upload_to='')),
            ],
        ),
    ]