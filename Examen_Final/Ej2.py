"""(3 ptos) Crear un programa para gestionar un fichero con diferentes
tipos de operaciones numéricas.
Reglas:
- El programa tendrá la función de crear el fichero con el nombre “notas.txt”
crearlo si no existe y el cual será dividido en dos archivos, uno principal
donde se llamará a las funciones que realizarán distintas operaciones en el
otro archivo la cual será llamada funciones.py.

- Crear una función donde se pedirá el tamaño de lista será ingresado por
consola (los números serán llenados de manera aleatoria dentro de la lista),
esta lista será escrita dentro del file “notas.txt”
- Crear una función donde se usará la librería math para obtener la raíz
cuadrada de los números que han sido llenados en la lista anterior y los
cuales serán escritos en el file “notas.txt”.

• Cerrar respectivamente los ficheros cada vez que se abra."""
from funciones import crear_lista, lista_raiz
while True:
    try:
        size = int(input("Ingrese el tamaño de la lista: "))
        break
    except ValueError:
        print("Ingrese un valor valido")
lista = crear_lista(size)
lista_cadena = [str(i) for i in lista]
cadena_final = " ".join(lista_cadena)
file1 = open("my_files/notas.txt", "w")
file1.write(cadena_final + "\n")
file1.close()

lista_raices = lista_raiz(lista)
lista_cadena1 = [str(i) for i in lista_raices]
cadena_final1 = " ".join(lista_cadena1)
file1 = open("my_files/notas.txt", "+a")
file1.write(cadena_final1)
file1.close()
