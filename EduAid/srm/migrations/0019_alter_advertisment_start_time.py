# Generated by Django 4.2.5 on 2024-02-25 16:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srm', '0018_alter_advertisment_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 25, 16, 36, 43, 494773, tzinfo=datetime.timezone.utc)),
        ),
    ]
