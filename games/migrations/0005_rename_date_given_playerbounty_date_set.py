# Generated by Django 4.0.3 on 2022-08-13 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_gamescript_report_bounty_gamescript_report_deadline_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playerbounty',
            old_name='date_given',
            new_name='date_set',
        ),
    ]
