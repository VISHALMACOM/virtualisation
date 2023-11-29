# Generated by Django 4.2.7 on 2023-11-21 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('time_table_id', models.IntegerField(primary_key=True, serialize=False)),
                ('day_of_week', models.CharField(max_length=10)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.class')),
            ],
        ),
    ]
