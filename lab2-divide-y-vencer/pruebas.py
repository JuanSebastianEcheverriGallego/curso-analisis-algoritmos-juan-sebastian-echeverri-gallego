"""Pruebas de las dos soluciones del subarreglo maximo."""

import random

from subarreglo import (subarreglo_fuerza_bruta, subarreglo_maximo,
                        suma_cruzada)


def suma_del_tramo(valores, inicio, fin):
    # Suma directa del tramo, para comprobar que los indices devueltos
    # corresponden a la suma devuelta.
    total = 0.0
    for i in range(inicio, fin + 1):
        total += valores[i]
    return total


def revisar(serie, esperado=None):
    copia = list(serie)
    bruta = subarreglo_fuerza_bruta(serie)
    dyv = subarreglo_maximo(serie, 0, len(serie) - 1)

    assert serie == copia, f"la lista fue modificada en {serie}"
    assert bruta[2] == dyv[2], f"sumas distintas en {serie}: {bruta} vs {dyv}"
    assert bruta[2] == suma_del_tramo(serie, bruta[0], bruta[1])
    assert dyv[2] == suma_del_tramo(serie, dyv[0], dyv[1])
    if esperado is not None:
        assert bruta[2] == esperado, f"esperaba {esperado} y dio {bruta[2]}"
    return bruta[2]


# 1. La serie de ocho dias de la situacion problema: la mejor racha va
#    del dia 2 al dia 7 y suma 17.
revisar([-3, 5, -2, 8, -6, 3, 9, -4], 17)

# 2. Series de un solo elemento, positivo y negativo.
revisar([7], 7)
revisar([-7], -7)

# 3. Todos los valores negativos: la mejor racha es el dia menos malo.
revisar([-5, -2, -9, -14], -2)
revisar([-1, -1, -1], -1)

# 4. Todos los valores positivos: la mejor racha es la serie completa.
revisar([1, 2, 3, 4], 10)
revisar([6, 6, 6], 18)

# 5. La mejor racha cruza el punto medio. Con cinco dias el medio es el
#    indice 2: la izquierda sola da 6, la derecha sola da 7 y el tramo
#    cruzado (indices 1 a 3) da 12.
revisar([-2, 6, -1, 7, -3], 12)
revisar([4, -10, 3, 3, -10, 4], 6)

# 6. suma_cruzada por separado: el mejor tramo que obligatoriamente
#    incluye al punto medio y el dia siguiente.
#    En la serie de ocho dias, con medio = 3, el tramo cruzado va de los
#    indices 1 a 6 y suma 17.
assert suma_cruzada([-3, 5, -2, 8, -6, 3, 9, -4], 0, 3, 7)[2] == 17
#    Con todos los valores negativos tiene que devolver los dos dias
#    menos malos, uno de cada lado, y no un tramo vacio.
assert suma_cruzada([-5, -2, -9, -14], 0, 1, 3)[2] == -11
#    Aqui el mejor tramo de toda la serie es el 9 solo, que esta en una
#    mitad; el cruzado esta obligado a tocar las dos y da 9 - 7 + 2 + 1.
assert suma_cruzada([9, -7, 2, 1, -8], 0, 2, 4)[2] == 5

# 7. Veinte listas aleatorias: las dos soluciones deben dar la misma
#    suma. Semilla fija para que la prueba sea reproducible.
generador = random.Random(7)
for caso in range(20):
    largo = generador.randint(1, 60)
    serie = [generador.randint(-100, 100) for _ in range(largo)]
    revisar(serie)

# 8. Listas aleatorias de un solo signo, que son los casos donde es mas
#    facil equivocarse con el caso base.
for caso in range(5):
    largo = generador.randint(1, 40)
    revisar([generador.randint(-100, -1) for _ in range(largo)])
    revisar([generador.randint(1, 100) for _ in range(largo)])

print("Todas las pruebas pasaron.")
