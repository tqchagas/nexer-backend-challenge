# -*- coding: utf-8 -*-
from api.models import Reserva as ReservaModel
from api.serializers import (
    ConsultaSerializer, ReservaSerializer
)
from api.utils import salvar_reservas

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class Reserva(APIView):

    def get(self, request):
        serializer = ConsultaSerializer(data=request.GET)
        if serializer.is_valid():
            reservas = salvar_reservas(
                serializer.validated_data.get('data')
            )
            serializer = ReservaSerializer(reservas, many=True)
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request):
        serializer = ConsultaSerializer(data=request.GET)
        if serializer.is_valid():
            data = serializer.validated_data.get('data')
            reservas = ReservaModel.objects.filter(
                consulta__data_consultada=data
            )
            reservas.delete()
            return Response(
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
