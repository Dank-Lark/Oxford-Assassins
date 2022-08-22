# Generated by Django 4.0.3 on 2022-08-18 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_rename_date_given_playerbounty_date_set'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='published',
            field=models.BooleanField(default=False, verbose_name='published'),
        ),
        migrations.AddField(
            model_name='gamescript',
            name='flags_used',
            field=models.ManyToManyField(to='games.flag'),
        ),
    ]
