# Generated by Django 4.1 on 2022-08-30 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Тип доставки')),
            ],
            options={
                'verbose_name': 'Тип доставки',
                'verbose_name_plural': 'Типы доставки',
                'db_table': 'table_007_delivery_type',
            },
        ),
        migrations.CreateModel(
            name='TypeOfCargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Тип груза')),
            ],
            options={
                'verbose_name': 'Тип груза',
                'verbose_name_plural': 'Типы груза',
                'db_table': 'table_006_types_of_cargo',
            },
        ),
        migrations.CreateModel(
            name='Urgency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Срочность доставки')),
            ],
            options={
                'verbose_name': 'Срочность доставки',
                'verbose_name_plural': 'Срочность доставки',
                'db_table': 'table_005_urgencies',
            },
        ),
    ]