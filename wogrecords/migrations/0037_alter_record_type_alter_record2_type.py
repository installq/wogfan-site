# Generated by Django 5.0.6 on 2024-07-29 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wogrecords', '0036_alter_record_type_alter_record2_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='Type',
            field=models.CharField(choices=[('B', 'Balls'), ('T', 'Time'), ('O', 'OCDTime'), ('M', 'Moves')], default='B', max_length=2),
        ),
        migrations.AlterField(
            model_name='record2',
            name='Type',
            field=models.CharField(choices=[('B', 'Balls'), ('T', 'Time'), ('O', 'OCDTime'), ('M', 'Moves')], default='B', max_length=2),
        ),
    ]