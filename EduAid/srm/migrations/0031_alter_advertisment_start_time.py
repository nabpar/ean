# Generated by Django 4.2.5 on 2024-03-05 14:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srm', '0030_alter_advertisment_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 5, 14, 25, 7, 896868, tzinfo=datetime.timezone.utc)),
        ),
    ]
