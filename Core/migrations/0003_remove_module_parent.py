# Generated by Django 4.1.1 on 2022-09-21 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_metric_frequency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='parent',
        ),
    ]