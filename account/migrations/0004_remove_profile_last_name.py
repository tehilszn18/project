# Generated by Django 4.1.7 on 2023-06-14 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_profile_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]
