from django.contrib import admin
from .models import UserPSG


class UserPSGAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_name', 'first_name', 'email', )
    readonly_fields = ('user', )


admin.site.register(UserPSG, UserPSGAdmin)

