# Generated by Django 4.2.1 on 2023-06-06 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_course_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='groups',
            field=models.ManyToManyField(default='', related_name='Курсы', to='main.studygroup'),
        ),
    ]
