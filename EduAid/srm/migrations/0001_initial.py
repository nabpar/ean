# Generated by Django 4.2.5 on 2023-12-25 16:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('area', models.CharField(choices=[('top', 'Top'), ('button', 'Button'), ('left', 'left'), ('right', 'Rignt')], default=1, max_length=255)),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('start_time', models.DateTimeField(default=datetime.datetime(2023, 12, 25, 16, 59, 10, 929973, tzinfo=datetime.timezone.utc))),
                ('end_time', models.DateTimeField()),
            ],
        ),
    ]
