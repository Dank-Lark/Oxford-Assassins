# Generated by Django 4.0.3 on 2022-08-18 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_assassin_cabal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assassin',
            old_name='startYear',
            new_name='start_year',
        ),
    ]
