from django.db import models


class Aeroporto(models.Model):

    def __init__(self, id, nome, codigo, estado, cidade, pais):
        self.id = id
        self.nome = nome
        self.codigo = codigo
        self.estado = estado
        self.cidade = cidade
        self.pais = pais
        super(Aeroporto).__init__()

    def __str__(self):
        return self.nome
    id = models.IntegerField
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)


class Voo(models.Model):

    def __init__(self, id, idAeroporto, data, horario, numero, origem, destino, portaoEmbarque, companhia):
        self.id = id
        self.idAeroporto = idAeroporto
        self.data = data
        self.horario = horario
        self.numero = numero
        self.origem = origem
        self.destino = destino
        self.portaoEmbarque = portaoEmbarque
        self.companhia = companhia
        super(Voo).__init__()

    id = models.IntegerField
    idAeroporto = models.IntegerField
    data = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    numero = models.IntegerField
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    portaoEmbarque = models.CharField(max_length=100)
    companhia = models.CharField(max_length=100)





# Create your models here.
