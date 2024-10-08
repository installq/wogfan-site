# Generated by Django 5.0.2 on 2024-02-24 04:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wogrecords', '0004_alter_level_options_remove_level_ballrec_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='BallRec',
        ),
        migrations.RemoveField(
            model_name='level',
            name='MoveRec',
        ),
        migrations.RemoveField(
            model_name='level',
            name='OCDTimeRec',
        ),
        migrations.RemoveField(
            model_name='level',
            name='TimeRec',
        ),
        migrations.AddField(
            model_name='level',
            name='BallRec',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Ball', to='wogrecords.record'),
        ),
        migrations.AddField(
            model_name='level',
            name='MoveRec',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Move', to='wogrecords.record'),
        ),
        migrations.AddField(
            model_name='level',
            name='OCDTimeRec',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='OCDTime', to='wogrecords.record'),
        ),
        migrations.AddField(
            model_name='level',
            name='TimeRec',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Time', to='wogrecords.record'),
        ),
    ]
