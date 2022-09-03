from django.contrib.auth.decorators import user_passes_test
from rest_framework import permissions


class IsCalcUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='CalcUsers').exists():
            return True
        return bool(request.user.is_superuser)


