# Generated by Django 2.2.3 on 2019-08-02 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_remove_room_rooms'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Room',
        ),
    ]
