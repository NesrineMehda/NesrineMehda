# Generated by Django 5.0.4 on 2024-04-30 07:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mother',
            name='child',
        ),
        migrations.AddField(
            model_name='child',
            name='motherID',
            field=models.ForeignKey(default='mother', on_delete=django.db.models.deletion.CASCADE, to='child.mother'),
        ),
    ]