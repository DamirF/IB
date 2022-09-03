import json

from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsCalcUser
from .psg_cse_api_tools import calc_func
from .psg_cse_api_tools.cse_to_db import send_calc_request
from .psg_cse_api_tools.pretty_response import transform_respone
from .serializers import CalcSerializer


class CalcCreateAPI(APIView):
    permission_classes = (IsCalcUser,)
    serializer_class = CalcSerializer
    # authentication_classes = (TokenAuthentication, )

    def post(self, request):
        serializer = CalcSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            new_calc = serializer.save()

            send_calc_request(sending_user=request.user.id,
                              city_sender=new_calc.sending_point,
                              city_recipient=new_calc.arrival_point,
                              urgency=new_calc.urgency,
                              type_of_cargo=new_calc.type_of_cargo,
                              delivery_type=new_calc.delivery_type,
                              lenght=new_calc.lenght,
                              width=new_calc.width,
                              height=new_calc.height,
                              weight=new_calc.weight,
                              is_test=new_calc.is_test,
                              declared_value_rate=new_calc.declared_value_rate
                              )

            return Response(json.loads(json.dumps(transform_respone(calc_func.ready_answer_calc_dict),
                                                  default=str, ensure_ascii=False, indent=2)
                                       )
                            )
        else:
            return Response({serializer.data})


def get_calc_interface(request):
    return render(request, "calc_interface_index.html", )
