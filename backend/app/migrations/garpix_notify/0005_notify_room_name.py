# Generated by Django 3.1 on 2022-02-02 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garpix_notify', '0004_auto_20220125_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='notify',
            name='room_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название комнаты'),
        ),
    ]
