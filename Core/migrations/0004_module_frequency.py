# Generated by Django 4.1.1 on 2022-09-21 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0003_remove_module_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='frequency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Core.frequency'),
        ),
    ]
