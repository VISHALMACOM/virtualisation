# Generated by Django 4.2.7 on 2023-11-21 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_timetable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('holiday_id', models.IntegerField(primary_key=True, serialize=False)),
                ('holiday_date', models.DateField()),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.IntegerField(primary_key=True, serialize=False)),
                ('room_name', models.CharField(max_length=6)),
                ('room_building', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='TimeTableEntry',
            fields=[
                ('entry_id', models.IntegerField(primary_key=True, serialize=False)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.course')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.room')),
                ('time_table_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.timetable')),
            ],
        ),
    ]
