# Generated by Django 4.2.1 on 2023-06-08 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('additional_information', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='mail',
            new_name='email',
        ),
    ]
