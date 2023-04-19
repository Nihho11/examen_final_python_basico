"""Aca van las funciones"""
import random
import math


def crear_lista(size):
    return [random.randint(0, 20) for i in range(size)]


def lista_raiz(lista):
    return [math.sqrt(i) for i in lista]
