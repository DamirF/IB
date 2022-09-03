from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import RegisterNewUser
from .models import UserPSG
from .sersializers import UserPSGSerializer


def registr_form(request):
    title = 'Авторизация'
    if request.method == 'POST':
        form = RegisterNewUser()
    return render(request, "registr_index.html", {'head_title': title})


class UserPSGRegistrationAPI(APIView):
    serializer_class = UserPSGSerializer
    permission_classes = (IsAdminUser, )

    def post(self, request):
        serializer = UserPSGSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save(is_staff=True)
            user_psg = UserPSG.create(user)
            user_psg.save()
            response = {
                "e-mail": user.email,
                "username": user.username,
                "id": user.id
            }
            return Response(response)
        else:
            return Response({serializer.data})





