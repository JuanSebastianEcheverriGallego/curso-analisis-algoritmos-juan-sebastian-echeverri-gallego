"""Generadores de lotes de registros para los escenarios de Tamiza."""

import random

# Los indices de riesgo van de 0 a 1000, pero para poder generar lotes
# grandes con valores distintos entre si se usa un rango proporcional a n.
FACTOR_RANGO = 10


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.

    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    generador = random.Random(semilla)
    return generador.sample(range(n * FACTOR_RANGO), n)


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.

    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98% en el orden que el algoritmo produce y el 2% restante
        desordenado al final.
    """
    generador = random.Random(semilla)
    corte = int(n * 0.98)
    # El 98% se construye directamente en orden descendente, restando un
    # salto aleatorio par: asi queda ordenado sin usar ninguna rutina de
    # ordenamiento y todos los valores son distintos entre si.
    valor = n * FACTOR_RANGO
    ordenados = []
    for _ in range(corte):
        valor -= 2 * generador.randint(1, FACTOR_RANGO // 2)
        ordenados.append(valor)
    # Los registros nuevos toman valores impares del mismo rango, asi que
    # no chocan con los anteriores y quedan repartidos por toda la lista.
    nuevos = generador.sample(range(valor + 1, n * FACTOR_RANGO, 2),
                              n - corte)
    return ordenados + nuevos


def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).

    Args:
        n: cantidad de registros del lote.

    Returns:
        Lista de n indices de riesgo enteros distintos, en el orden
        inverso al que el algoritmo debe producir.
    """
    return list(range(0, n * FACTOR_RANGO, FACTOR_RANGO))
