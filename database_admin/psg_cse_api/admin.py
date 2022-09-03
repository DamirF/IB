from django.contrib import admin
from .models import Calc

# Register your models here.


class CalcAdmin(admin.ModelAdmin):
    list_display = ('id', 'sending_point', 'arrival_point', 'lenght', 'width', 'height', 'weight',
                    'declared_value_rate', 'insurance_rate', 'urgency_display', 'type_of_cargo_display',
                    'delivery_type_display', 'is_test', )
    readonly_fields = list_display


admin.site.register(Calc, CalcAdmin)


