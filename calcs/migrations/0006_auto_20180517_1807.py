# Generated by Django 2.0.5 on 2018-05-17 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calcs', '0005_remove_measure_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measure',
            name='exist_reason',
        ),
        migrations.AddField(
            model_name='measure',
            name='exit_reason',
            field=models.CharField(default='default', max_length=200),
        ),
        migrations.AddField(
            model_name='measure',
            name='method',
            field=models.CharField(choices=[('gs', 'global_search'), ('pi', 'piyavsky')], default='gs', max_length=2),
        ),
    ]
