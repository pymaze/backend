# Generated by Django 2.2.3 on 2019-07-31 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_auto_20190730_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='e',
        ),
        migrations.RemoveField(
            model_name='room',
            name='e_to',
        ),
        migrations.RemoveField(
            model_name='room',
            name='n',
        ),
        migrations.RemoveField(
            model_name='room',
            name='n_to',
        ),
        migrations.RemoveField(
            model_name='room',
            name='s',
        ),
        migrations.RemoveField(
            model_name='room',
            name='s_to',
        ),
        migrations.RemoveField(
            model_name='room',
            name='w',
        ),
        migrations.RemoveField(
            model_name='room',
            name='w_to',
        ),
        migrations.AddField(
            model_name='room',
            name='rooms',
            field=models.CharField(default='[[{}]]', max_length=5000000),
        ),
    ]