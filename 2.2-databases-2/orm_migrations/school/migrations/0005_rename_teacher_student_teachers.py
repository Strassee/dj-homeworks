# Generated by Django 4.2.6 on 2023-11-12 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_rename_teachers_student_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teacher',
            new_name='teachers',
        ),
    ]