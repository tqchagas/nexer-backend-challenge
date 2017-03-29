# -*- coding: utf-8 -*-
from django.test import TestCase

from api.utils import buscar_reservas


class ReservasTestCase(TestCase):
    def test_reservas(self):
        data = '2017-05-01'
        self.assertGreater(len(buscar_reservas(data)), 0)

    def test_reservas_data_invalida(self):
        data = '2010-05-01'
        self.assertEqual(len(buscar_reservas(data)), 0)

    def test_reservas_timeout(self):
        data = '2017-05-01'
        self.assertRaises(
            Exception,
            buscar_reservas,
            data,
            '0.0001'
        )
