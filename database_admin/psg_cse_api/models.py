from django.db import models
from django.contrib import admin

from info_guides.models import Urgency, TypeOfCargo, DeliveryType


class Calc(models.Model):
    sending_point = models.CharField(max_length=150, verbose_name='Город отправки')
    arrival_point = models.CharField(max_length=150, verbose_name='Город прибытия')
    urgency = models.ForeignKey(Urgency, on_delete=models.CASCADE, verbose_name='Срочность доставки',
                                blank=False, null=True)
    type_of_cargo = models.ForeignKey(TypeOfCargo, on_delete=models.CASCADE, verbose_name='Тип груза',
                                      blank=False, null=True)
    weight = models.FloatField(verbose_name='Вес')
    lenght = models.FloatField(verbose_name='Длина')
    width = models.FloatField(verbose_name='Ширина')
    height = models.FloatField(verbose_name='Высота')
    delivery_type = models.ForeignKey(DeliveryType, on_delete=models.CASCADE, verbose_name='Тип доставки',
                                      blank=False, null=True)
    declared_value_rate = models.IntegerField(verbose_name='Объявленная стоимость груза', blank=False, null=True)
    insurance_rate = models.IntegerField(verbose_name='Страховая стоимость груза', blank=False, null=True)

    is_test = models.BooleanField(default=False, verbose_name='Тестовая версия')

    class Meta:
        db_table = 'table_004_calc_parameters'

    @admin.display(description='Срочность доставки')
    def urgency_display(self):
        if self.urgency is None:
            return 'Не указан'
        return str(self.urgency)

    @admin.display(description='Тип груза')
    def type_of_cargo_display(self):
        if self.type_of_cargo is None:
            return 'Не указан'
        return str(self.type_of_cargo)

    @admin.display(description='Тип доставки')
    def delivery_type_display(self):
        if self.delivery_type is None:
            return 'Не указан'
        return str(self.delivery_type)
