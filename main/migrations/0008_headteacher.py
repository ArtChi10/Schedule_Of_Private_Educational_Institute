# Generated by Django 4.2.1 on 2023-06-04 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_classroom_lesson'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeadTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Заведующий учебной частью',
                'verbose_name_plural': 'Заведущие учебной частью',
            },
        ),
    ]
