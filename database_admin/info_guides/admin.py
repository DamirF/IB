from django.contrib import admin

# Register your models here.
from info_guides.models import Urgency, TypeOfCargo, DeliveryType


class UrgencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )


class TypeOfCargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )


class DeliveryTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )


admin.site.register(Urgency, UrgencyAdmin)
admin.site.register(TypeOfCargo, TypeOfCargoAdmin)
admin.site.register(DeliveryType, DeliveryTypeAdmin)