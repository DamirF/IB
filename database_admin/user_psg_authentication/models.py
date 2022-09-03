from django.contrib.auth.models import User
from django.contrib import admin
from django.db import models


class UserPSG(models.Model):

    class Meta:
        verbose_name = 'Пользователь PSG'
        verbose_name_plural = 'Пользователи PSG'
        db_table = 'table_003_users_psg'

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def create(cls, user: User):
        user_psg = cls(user=user)
        return user_psg

    @classmethod
    def delete(self, *args, **kwargs):
        User.objects.filter(id=self.user.id).delete()
        super(UserPSG, self).delete(*args, **kwargs)

    def __str__(self):
        return self.user.username

    @admin.display(description="Login")
    def username(self):
        return self.user.username

    @admin.display(description="Имя")
    def first_name(self):
        return self.user.first_name

    @admin.display(description="Фамилия")
    def last_name(self):
        return self.user.last_name

    @admin.display(description="Email")
    def email(self):
        return self.user.email
