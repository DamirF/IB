from django.db import models

# Create your models here.


class Urgency(models.Model):
    name = models.CharField(max_length=150, verbose_name='Срочность доставки')

    class Meta:
        verbose_name = 'Срочность доставки'
        verbose_name_plural = 'Срочность доставки'
        db_table = 'table_005_urgencies'

    def __str__(self):
        return self.name


class TypeOfCargo(models.Model):
    name = models.CharField(max_length=150, verbose_name='Тип груза')

    class Meta:
        verbose_name = 'Тип груза'
        verbose_name_plural = 'Типы груза'
        db_table = 'table_006_types_of_cargo'

    def __str__(self):
        return self.name


class DeliveryType(models.Model):
    name = models.CharField(max_length=150, verbose_name='Тип доставки')

    class Meta:
        verbose_name = 'Тип доставки'
        verbose_name_plural = 'Типы доставки'
        db_table = 'table_007_delivery_type'

    def __str__(self):
        return self.name
