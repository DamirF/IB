from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class RequestResponse(models.Model):
    class Meta:
        db_table = 'table_001_request_response'
        verbose_name = 'HTTP - запрос'
        verbose_name_plural = 'HTTP - запросы'

    api_http_request = models.TextField(verbose_name="HTTP-запрос")
    print("Задали параметр запроса в API Agora: api_http_request = models.JSONField(verbose_name=\"HTTP-запрос\") = " +
          str(api_http_request.verbose_name))
    api_http_response = models.TextField(verbose_name="Ответ сервера")
    print(
        "Получили ответ на запрос в API Agora: api_http_respone = models.JSONField(verbose_name=\"Ответ сервера\") = " +
        str(api_http_response.verbose_name))
    api_http_request_send_time = models.DateTimeField(verbose_name="Время отправки запроса")
    print(
        "Фиксируем время отправки запроса: api_http_request_send_time = models.DateTimeField(verbose_name=\""
        "Время отправки запроса\") = " +
        str(api_http_request_send_time.verbose_name))
    api_http_response_waiting_time = models.CharField(max_length=10, verbose_name="Время ожидания ответа")
    print(
        "Фиксируем время ожидания ответа на запрос: api_http_response_waiting_time = "
        "models.CharField(verbose_name=\"Время ожидания ответа\") = " +
        str(api_http_response_waiting_time.verbose_name))

    user_id = models.ForeignKey(User, verbose_name="Отправитель", on_delete=models.PROTECT)
    print(
        "Фиксируем ID отправителя запроса: user_id = models.IntegerField(verbose_name=\"ID отправителя\") = " +
        str(user_id.verbose_name))

    @admin.display(description='Фамилия')
    def sending_user_last_name(self):
        return self.user_id.last_name

    @admin.display(description='Имя')
    def sending_user_first_name(self):
        return self.user_id.first_name

    @admin.display(description='Почта')
    def sending_user_email(self):
        return self.user_id.email
