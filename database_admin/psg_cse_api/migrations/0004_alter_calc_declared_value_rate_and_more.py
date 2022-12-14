# Generated by Django 4.1 on 2022-08-30 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psg_cse_api', '0003_alter_calc_delivery_type_alter_calc_type_of_cargo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calc',
            name='declared_value_rate',
            field=models.IntegerField(null=True, verbose_name='Объявленная стоимость груза'),
        ),
        migrations.AlterField(
            model_name='calc',
            name='insurance_rate',
            field=models.IntegerField(null=True, verbose_name='Страховая стоимость груза'),
        ),
    ]
