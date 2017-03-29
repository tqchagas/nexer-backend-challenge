# -*- coding: utf-8 -*-
from api.models import Reserva

from rest_framework import serializers


class ConsultaSerializer(serializers.Serializer):
    data = serializers.DateField(required=True)


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva

        fields = (
            'modelo',
        )
