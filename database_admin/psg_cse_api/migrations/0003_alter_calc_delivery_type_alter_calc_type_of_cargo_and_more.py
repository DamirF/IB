# Generated by Django 4.1 on 2022-08-30 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info_guides', '0001_initial'),
        ('psg_cse_api', '0002_rename_wight_calc_width_alter_calc_is_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calc',
            name='delivery_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='info_guides.deliverytype', verbose_name='Тип доставки'),
        ),
        migrations.AlterField(
            model_name='calc',
            name='type_of_cargo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='info_guides.typeofcargo', verbose_name='Тип груза'),
        ),
        migrations.AlterField(
            model_name='calc',
            name='urgency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='info_guides.urgency', verbose_name='Срочность доставки'),
        ),
    ]