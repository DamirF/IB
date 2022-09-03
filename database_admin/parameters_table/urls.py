from django.contrib.auth.decorators import user_passes_test
from django.urls import path
from .views import get_params_table

urlpatterns = [
    path('admin-show_params_table/', user_passes_test(lambda u: u.is_superuser)(get_params_table),
         name='admin-show_params_table'),
]