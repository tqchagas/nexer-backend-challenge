# -*- coding: utf-8 -*-
from django.db import models


class Consulta(models.Model):
    realizada_em = models.DateTimeField(
        auto_now_add=True
    )
    data_consultada = models.DateField(
        null=False,
        blank=False
    )
    expirada = models.BooleanField(
        default=False
    )


class Modelo(models.Model):
    nome = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    montadora = models.ForeignKey(
        'Montadora',
        null=False,
        blank=False,
    )

    def __unicode__(self):
        return u"{nome}".format(nome=self.nome)


class Montadora(models.Model):
    nome = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    def __unicode__(self):
        return u"{nome}".format(nome=self.nome)


class Reserva(models.Model):
    consulta = models.ForeignKey(
        'Consulta',
        null=False,
        blank=False
    )
    modelo = models.ForeignKey(
        Modelo,
        null=False,
        blank=False
    )

    def __unicode__(self):
        return "{modelo} - {consulta}".format(
            modelo=self.modelo.nome,
            consulta=self.consulta.data_consultada.strftime('%d/%m/%Y')
        )
