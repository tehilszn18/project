# Generated by Django 4.1.7 on 2023-08-08 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_profile_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='highest_level_of_education',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='id_image',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='id_number',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='id_type',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lga_origin',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lga_residence',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_pics',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='state_of_origin',
        ),
    ]
