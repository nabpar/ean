# Generated by Django 4.2.5 on 2024-01-04 05:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srm', '0004_alter_advertisment_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 5, 55, 5, 302107, tzinfo=datetime.timezone.utc)),
        ),
    ]
