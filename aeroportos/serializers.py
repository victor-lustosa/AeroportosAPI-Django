from rest_framework import serializers
from .models import *


class AeroportoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Aeroporto
        fields = ('id', 'nome', 'codigo', 'cidade', 'estado', 'pais')


class VooSerializer (serializers.ModelSerializer):
    class Meta:
        model = Voo
        fields = ('id', 'idAeroporto','data', 'horario', 'numero', 'origem', 'destino','portaoEmbarque','companhia')
