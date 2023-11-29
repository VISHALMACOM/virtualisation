# Generated by Django 4.2.7 on 2023-11-21 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('attendance_id', models.IntegerField(primary_key=True, serialize=False)),
                ('attendance_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(default='ABSENT', max_length=10)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.class')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.student')),
            ],
        ),
    ]
