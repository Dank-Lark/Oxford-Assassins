# Generated by Django 4.0.3 on 2022-07-19 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_assassin_room_alter_assassin_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='registered',
            field=models.BooleanField(default=False, verbose_name='registered assassin'),
        ),
    ]
