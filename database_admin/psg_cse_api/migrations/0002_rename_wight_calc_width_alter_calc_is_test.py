# Generated by Django 4.1 on 2022-08-30 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psg_cse_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calc',
            old_name='wight',
            new_name='width',
        ),
        migrations.AlterField(
            model_name='calc',
            name='is_test',
            field=models.BooleanField(default=False, verbose_name='Тестовая версия'),
        ),
    ]
