# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from api.views import Reserva


urlpatterns = patterns(
    '',
    url(r'^reservas/$', Reserva.as_view(), name='reservas'),
)
