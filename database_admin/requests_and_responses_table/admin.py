import json
from django.contrib import admin

from .models import RequestResponse


# Register your models here.


class RequestResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'show_request_short', 'show_response_short', 'api_http_request_send_time',
                    'api_http_response_waiting_time', 'user_id', 'sending_user_last_name', 'sending_user_first_name',
                    'sending_user_email')
    list_filter = ('user_id', 'api_http_request_send_time')
    list_editable = ('user_id', )
    readonly_fields = ('api_http_request_send_time', 'api_http_response_waiting_time', 'user_id', )

    def show_request_short(self, obj):
        result = str(obj.api_http_request)[:50] + "......"
        return result
    show_request_short.short_description = "HTTP - запрос"

    def show_response_short(self, obj):
        result = str(obj.api_http_response)[:50] + "......"
        return result
    show_response_short.short_description = "Ответ"


admin.site.register(RequestResponse, RequestResponseAdmin)
