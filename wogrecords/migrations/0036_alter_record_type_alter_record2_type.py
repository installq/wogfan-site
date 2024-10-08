# Generated by Django 5.0.2 on 2024-07-28 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wogrecords', '0035_alter_record_type_record2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='Type',
            field=models.CharField(choices=[('O', 'OCDTime'), ('M', 'Moves'), ('T', 'Time'), ('B', 'Balls')], default='B', max_length=2),
        ),
        migrations.AlterField(
            model_name='record2',
            name='Type',
            field=models.CharField(choices=[('O', 'OCDTime'), ('M', 'Moves'), ('T', 'Time'), ('B', 'Balls')], default='B', max_length=2),
        ),
    ]
