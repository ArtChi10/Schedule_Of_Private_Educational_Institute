# Generated by Django 4.2.1 on 2023-06-14 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_alter_lesson_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='is_editing',
            field=models.BooleanField(default=False),
        ),
    ]
