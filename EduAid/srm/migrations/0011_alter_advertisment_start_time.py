# Generated by Django 4.2.5 on 2024-01-06 18:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srm', '0010_alter_advertisment_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 6, 18, 44, 23, 671911, tzinfo=datetime.timezone.utc)),
        ),
    ]
