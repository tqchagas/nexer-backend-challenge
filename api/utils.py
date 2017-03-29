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


def salvar_reservas(data):
    # salva os dados da reserva de uma data
    reservas, carros_reservados = buscar_reservas(data), []
    consulta = Consulta.objects.create(data_consultada=data)
    for reserva in reservas:
        obj_montadora, criado = Montadora.objects.get_or_create(
            nome=reserva.get('brand')
        )
        obj_modelo, criado = Modelo.objects.get_or_create(
            nome=reserva.get('model'),
            montadora=obj_montadora
        )
        reserva = Reserva(
            consulta=consulta,
            modelo=obj_modelo,
        )
        carros_reservados.append(reserva)

    return Reserva.objects.bulk_create(carros_reservados)


def consultar_reservas(data):
    agora = timezone.now()
    agora = agora - timezone.timedelta(seconds=120)
    consulta = Consulta.objects.filter(
        data_consultada=data,
        expirada=False,
        realizada_em__gt=agora
    )
    consulta.update(expirada=True)
    return consulta.first()
