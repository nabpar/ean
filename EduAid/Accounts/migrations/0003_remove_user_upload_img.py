# Generated by Django 4.2.5 on 2023-12-04 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_user_upload_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='upload_img',
        ),
    ]
