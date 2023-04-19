"""Escribir un programa para el manejo de listas el cuál cumplirá los
siguientes requerimientos (4 ptos):
Reglas:
- Crear una función que le permitirá almacenar 10 número aleatorios en una
lista y finalmente los imprimirá por consola al llamar la función.
- Crear una función que le permita almacenar los números no repetidos de la
lista anterior, retornar este valor e imprimirlo por consola.
- Crear una función donde se creará una lista para ordenar de mayor a menor
la lista que se creó en el ítem anterior (número no repetidos) y otra lista
para ordenarlas de menor a mayor, retornar este valor e imprimirlos por
consola.
- Crear una función para indicar cuál es mayor número de la lista (lista del
ítem 2), retornar este valor e imprimirlo por consola."""

import random


def num_aleatorios():
    return [random.randint(0, 10) for i in range(10)]


lista1 = num_aleatorios()
print("La lista de números aleatorios es: ", lista1)


def orden_sin_rep(lista):
    return list(set(lista))


lista1_limpia = orden_sin_rep(lista1)
print("La lista sin repetir números es: ", lista1_limpia)


def mayor_a_menor(lista):
    return sorted(lista, reverse=True)


lista1_ordenada = mayor_a_menor(lista1_limpia)
print("La lista ordenada de mayor a menor es: ", lista1_ordenada)


def menor_a_mayor(lista):
    return sorted(lista)


print("La lista ordenadar de menor a mayor es: ", menor_a_mayor(lista1_limpia))


def mayor_num(lista):
    return mayor_a_menor(lista)[0]


print("El mayor valor de la lista es: ", mayor_num(lista1_limpia))
