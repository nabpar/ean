# Generated by Django 4.2.5 on 2023-12-03 10:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='upload_img',
            field=models.ImageField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator('((.png)|(.jpeg)|(.heic))', message='Invalid image extension.....')]),
        ),
    ]
