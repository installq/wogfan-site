# Generated by Django 5.0.2 on 2024-06-20 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wogrecords', '0031_alter_record_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='Type',
            field=models.CharField(choices=[('T', 'Time'), ('B', 'Balls'), ('O', 'OCDTime'), ('M', 'Moves')], default='B', max_length=2),
        ),
    ]
