# Generated by Django 5.0.2 on 2024-02-25 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wogrecords', '0005_remove_level_ballrec_remove_level_moverec_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='record',
            options={'ordering': ['-Date']},
        ),
        migrations.AddField(
            model_name='record',
            name='Link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='Date',
            field=models.DateField(blank=True, null=True, verbose_name='Date Achieved'),
        ),
        migrations.AlterField(
            model_name='record',
            name='Player',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Player Name'),
        ),
        migrations.AlterField(
            model_name='record',
            name='Type',
            field=models.CharField(choices=[('T', 'Time'), ('M', 'Moves'), ('B', 'Balls'), ('O', 'OCDTime')], default='B', max_length=2),
        ),
    ]
