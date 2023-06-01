# Generated by Django 4.2.1 on 2023-06-01 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_course_studygroup_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Практика', max_length=50, verbose_name='Учебный предмет')),
            ],
            options={
                'verbose_name': 'Учебный предмет',
                'verbose_name_plural': 'Учебные предметы',
            },
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Курс', 'verbose_name_plural': 'Курсы'},
        ),
        migrations.AlterModelOptions(
            name='studygroup',
            options={'verbose_name': 'Учебная группа', 'verbose_name_plural': 'Учебные группы'},
        ),
    ]