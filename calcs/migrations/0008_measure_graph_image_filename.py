# Generated by Django 2.0.5 on 2018-05-18 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calcs', '0007_remove_measure_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='measure',
            name='graph_image_filename',
            field=models.CharField(default='', max_length=200),
        ),
    ]
