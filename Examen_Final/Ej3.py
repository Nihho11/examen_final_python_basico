"""(3 ptos) Crear un programa usando decoradores para medir el tiempo de
ejecución.
Reglas:
- Crear la función decorador adecuadamente que sumará los elementos de la
función que pasará como parámetro de la función decoradora
- Crear una función, por ejemplo, multiplicación de 4 números para decorarla
con la función anterior.
- Usar la propiedad de N parámetros para la función a decorar (*, **) y
visualizar los resultados con un mínimo tres ejemplos."""
import time


def funcion_decoradora(multiplicar):
    def funcion_decorada(*args, **kwargs):
        print("La suma de los elementos que se multiplicaran por "
              "la función es: ", sum(args))
        inicio = time.time()
        print("La función decorada nos da el producto de los números "
              "seleccionados: ", multiplicar(*args, **kwargs))
        fin = time.time()
        print("El tiempo de ejecución de la función decorada es: ",
              fin - inicio)
    return funcion_decorada


@funcion_decoradora
def multiplicar(*args):
    producto = 1
    for i in args:
        producto *= i
    return producto


multiplicar(1, 2, 5, 10, 100)
multiplicar(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
multiplicar(3, 10, 203, 233, 41, 20, 4)
multiplicar(1, 2)
multiplicar(9, 2, 3, 2, 5)
