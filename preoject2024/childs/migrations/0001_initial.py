# Generated by Django 5.0.4 on 2024-05-03 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('gendre', models.CharField(choices=[('boy', 'boy'), ('girl', 'girl')], max_length=10)),
                ('DateofBirth', models.DateField()),
                ('height', models.FloatField()),
                ('wieght', models.FloatField()),
            ],
        ),
    ]
