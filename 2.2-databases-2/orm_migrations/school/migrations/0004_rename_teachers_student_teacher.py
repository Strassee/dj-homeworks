# Generated by Django 4.2.6 on 2023-11-12 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_remove_student_teacher_student_teachers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teachers',
            new_name='teacher',
        ),
    ]