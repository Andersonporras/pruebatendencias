from time import perf_counter
from time import perf_counter_ns
from random import randint
from time import time_ns
from time import time


def llenar(arr, lon):
    for i in range(lon):
        arr.append(randint(0, 200) - 100)


def busqueda_binarias(lista, x, verbose=True):
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1  # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio  # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1  # descarto mitad derecha
        else:  # if lista[medio] < x:
            izq = medio + 1  # descarto mitad izquierda
    return pos


# Código para probar la búsqueda binaria
def main():
    lista = []
    llenar(lista, 500)
    tic1 = perf_counter_ns()
    x = 20
    resultado = busqueda_binarias(lista, x)
    print("Tiempo Calculado ", perf_counter_ns() - tic1)
    print("Resultado:", resultado)
    print("Resultado:", resultado)
    print("Resultado:", resultado)
# anderson porras rios

main()