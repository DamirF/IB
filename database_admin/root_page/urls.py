from django.contrib.auth.decorators import user_passes_test
from django.urls import path
from .views import get_root_page

urlpatterns = [
    path('', get_root_page)
]