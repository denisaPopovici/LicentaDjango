# Generated by Django 3.2 on 2022-04-07 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Licenta', '0015_visitedlocations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='', max_length=150)),
                ('notified', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notified', to='Licenta.customuser')),
                ('notifying', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifying', to='Licenta.customuser')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Licenta.post')),
            ],
        ),
    ]
