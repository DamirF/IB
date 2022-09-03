from django.urls import path, include
from .views import UserPSGRegistrationAPI, registr_form

urlpatterns = [
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/users_psg/registration/', UserPSGRegistrationAPI.as_view()),
    path('registration/', registr_form),
]