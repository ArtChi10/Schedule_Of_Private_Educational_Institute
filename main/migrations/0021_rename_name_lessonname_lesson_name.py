# Generated by Django 4.2.1 on 2023-06-09 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_advuser_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lessonname',
            old_name='name',
            new_name='lesson_name',
        ),
    ]
