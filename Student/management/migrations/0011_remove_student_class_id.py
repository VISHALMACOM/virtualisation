# Generated by Django 4.2.7 on 2023-11-24 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0010_alter_student_student_id_alter_users_student_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='class_id',
        ),
    ]
