# Generated by Django 4.2.1 on 2023-06-10 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_remove_studygroupschedule_schedule_of_course_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': 'Занятие', 'verbose_name_plural': 'Занятия'},
        ),
    ]
