from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from unidecode import unidecode

from aeroportos.models import Aeroporto, Voo
from aeroportos.serializers import AeroportoSerializer, VooSerializer

aeroporto1 = Aeroporto(1, 'Congonhas', 'AA36', 'São Paulo', 'São Paulo', 'Brasil')
aeroporto2 = Aeroporto(2, 'Santos Drumont', 'BB55', 'Rio de Janeiro', 'Rio de Janeiro', 'Brasil')
aeroporto3 = Aeroporto(3, 'Lysias Rodrigues', 'WW55', 'Palmas', 'Tocantins', 'Brasil')
aeroporto4 = Aeroporto(4, 'Pinto Martins', 'TT77', 'Fortaleza', 'Ceara', 'Brasil')
aeroporto5 = Aeroporto(5, 'Campo de Marte', 'AA46', 'São Paulo', 'São Paulo', 'Brasil')
aeroporto6 = Aeroporto(6, 'São José dos Campos', 'AA56', 'São Paulo', 'São Paulo', 'Brasil')

voo1 = Voo(1, 3, "10/10/2021", "14:12", 54873, "Palmas", "São Paulo", "AD52993", "TAM")
voo2 = Voo(2, 3, "10/10/2021", "14:12", 54873, "Palmas", "Fortaleza", "AD5798", "GOl")
voo3 = Voo(3, 1, "10/10/2021", "14:12", 54873, "São Paulo", "Palmas", "AD5663", "TAM")
voo4 = Voo(4, 1, "10/10/2021", "14:12", 54873, "São Paulo", "Rio de Janeiro", "AD5263", "TAM")
voo5 = Voo(5, 5, "10/10/2021", "14:12", 54873, "São Paulo", "Palmas", "AD578", "TAM")
voo6 = Voo(6, 6, "10/10/2021", "14:12", 54873, "São Paulo", "Fortaleza", "AD5645", "TAM")

listaVoo = [voo1, voo2, voo3, voo4, voo5, voo6]
listaAeroporto = [aeroporto1, aeroporto2, aeroporto3, aeroporto4, aeroporto5, aeroporto6]


class AeroportoDados(APIView):
    def get(self, request, cidade, estado):
        try:
            if id == None:
                return JsonResponse({'mensagem: ': "o id nao pode ser nulo"}, status=status.HTTP_400_BAD_REQUEST)
            listaAeroportoPesquisa = []
            for i in listaAeroporto:
                if i.cidade == cidade and i.estado == estado:
                    listaAeroportoPesquisa.append(i)

            serializer = AeroportoSerializer(listaAeroportoPesquisa, many=True)
            return Response(serializer.data)
        except Exception:
            return JsonResponse({'mensagem: ': "ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class VooDados(APIView):
    def get(self, request, id):
        try:
            if id == None:
                return JsonResponse({'mensagem: ': "o id nao pode ser nulo"}, status=status.HTTP_400_BAD_REQUEST)
            listaVooId = []
            for i in listaVoo:
                if i.idAeroporto == int(id):
                   listaVooId.append(i)

            serializer = VooSerializer(listaVooId, many=True)
            return Response(serializer.data)
        except Exception:
            return JsonResponse({'mensagem: ': "ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# Create your views here.
