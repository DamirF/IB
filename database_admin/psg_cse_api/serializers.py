from rest_framework import serializers

from info_guides.models import Urgency, TypeOfCargo, DeliveryType
from .models import Calc


class CalcSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Calc.objects.create(**validated_data)

    class Meta:
        model = Calc
        fields = '__all__'
