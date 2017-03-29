# -*- coding: utf-8 -*-
import requests

from django.utils import timezone

from api.models import (
    Consulta, Modelo, Montadora, Reserva
)


def buscar_reservas(data, timeout=5):
    # efetua requisição GET e retorna reserva de uma data
    url = "https://demo8306178.mockable.io/hipotetica/car-renting/{data}/"
    url = url.format(data=data)
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            return response.json().get('cars')
        return []
    except requests.exceptions.ConnectionError:
        raise Exception("Erro de conexão")
