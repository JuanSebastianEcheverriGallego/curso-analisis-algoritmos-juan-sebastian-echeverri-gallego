"""Medicion comparativa de la Parte 4: insertion sort contra merge sort.

Los dos algoritmos se ejecutan sobre el escenario A de Tamiza (lote en
orden aleatorio), con los mismos tamanos de entrada de la Parte 3, y se
grafica el tiempo de ejecucion de cada uno en los mismos ejes.
"""

import time
import tracemalloc
from collections.abc import Callable
from statistics import median

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio

TAMANIOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3
REPETICIONES_FINAS = 25
SEMILLA = 42

ALGORITMOS = [
    ("Insertion sort", insertion_sort, "#0072B2", "o"),
    ("Merge sort", merge_sort, "#D55E00", "s"),
]


def medir(
    algoritmo: Callable[[list[int]], tuple[list[int], int]],
    lote: list[int]
) -> tuple[float, int]:
    """Mide el tiempo de un algoritmo sobre un lote ya construido.

    El lote se genera antes de llamar a esta funcion para que el
    cronometro solo cubra la ejecucion del algoritmo.

    Args:
        algoritmo: funcion de ordenamiento instrumentada.
        lote: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con el tiempo mediano en milisegundos de
        REPETICIONES corridas y el numero de comparaciones.
    """
    tiempos = []
    comparaciones = 0
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        _, comparaciones = algoritmo(lote)
        fin = time.perf_counter()
        tiempos.append((fin - inicio) * 1000)
    return median(tiempos), comparaciones


def correr_experimento() -> dict[str, list[float]]:
    """Mide los dos algoritmos sobre el escenario A en todos los tamanos.

    Returns:
        Diccionario con el nombre del algoritmo como clave y la lista
        de tiempos medianos como valor.
    """
    resultados = {}
    for nombre, algoritmo, _, _ in ALGORITMOS:
        tiempos = []
        for n in TAMANIOS:
            lote = generar_aleatorio(n, SEMILLA)
            tiempo, comps = medir(algoritmo, lote)
            tiempos.append(tiempo)
            print(f"{nombre:15s} n={n:5d} {comps:12d} comp "
                  f"{tiempo:9.2f} ms")
        resultados[nombre] = tiempos
    return resultados


def graficar(resultados: dict[str, list[float]], archivo: str) -> None:
    """Dibuja el tiempo de los dos algoritmos en los mismos ejes.

    Args:
        resultados: salida de correr_experimento().
        archivo: ruta del archivo PNG de salida.
    """
    figura, ejes = plt.subplots(figsize=(8, 5))
    for nombre, _, color, marca in ALGORITMOS:
        ejes.plot(TAMANIOS, resultados[nombre], marker=marca, markersize=8,
                  linewidth=2, color=color, label=nombre)
    ejes.set_title("Escenario A: tiempo de ejecución vs. tamaño de entrada")
    ejes.set_xlabel("Tamaño de entrada n (número de registros)")
    ejes.set_ylabel("Tiempo de ejecución (milisegundos)")
    ejes.grid(True, linewidth=0.5, alpha=0.4)
    ejes.legend(title="Algoritmo")
    figura.tight_layout()
    figura.savefig(archivo, dpi=150)
    plt.close(figura)
    print(f"Grafica guardada en {archivo}")


def comprobar_mejor_caso() -> None:
    """Comprueba que el mejor caso de insertion sort cuesta n - 1.

    Respalda la afirmacion de la seccion 4.1 del informe. El lote se
    construye ya en orden descendente, que es el orden que el algoritmo
    produce, asi que ningun elemento debe moverse.
    """
    lote = list(range(1000, 0, -10))
    _, comparaciones = insertion_sort(lote)
    print(f"Mejor caso: n={len(lote)}  comparaciones={comparaciones}  "
          f"esperado={len(lote) - 1}")


def comprobar_cruce_tamanos_pequenos() -> None:
    """Mide los dos algoritmos en tamanos pequenos para ver el cruce.

    Respalda la afirmacion de la seccion 4.2 sobre el tamano a partir
    del cual merge sort se vuelve mas rapido que insertion sort. Usa
    mas repeticiones que el experimento principal porque los tiempos
    estan en microsegundos.
    """
    print("Cruce en tamanos pequenos (escenario A, mediana de "
          f"{REPETICIONES_FINAS} corridas):")
    for n in (20, 40, 50, 60, 80, 100):
        lote = generar_aleatorio(n, SEMILLA)
        tiempos_insercion = []
        tiempos_mezcla = []
        for _ in range(REPETICIONES_FINAS):
            inicio = time.perf_counter()
            insertion_sort(lote)
            tiempos_insercion.append((time.perf_counter() - inicio) * 1e6)
            inicio = time.perf_counter()
            merge_sort(lote)
            tiempos_mezcla.append((time.perf_counter() - inicio) * 1e6)
        insercion = median(tiempos_insercion)
        mezcla = median(tiempos_mezcla)
        gana = "insertion" if insercion < mezcla else "merge"
        print(f"  n={n:4d}  insertion={insercion:7.1f} us  "
              f"merge={mezcla:7.1f} us  gana {gana}")


def comprobar_merge_sort_grande() -> None:
    """Mide merge sort en un lote grande y su pico de memoria.

    Respalda las dos cifras del concepto tecnico de la seccion 4.3: el
    tiempo de una corrida con 200.000 registros y la memoria adicional
    que consume la mezcla, medida con tracemalloc.
    """
    lote = generar_aleatorio(200000, SEMILLA)
    inicio = time.perf_counter()
    merge_sort(lote)
    tiempo = (time.perf_counter() - inicio) * 1000
    print(f"Merge sort con n=200000: {tiempo:.1f} ms en una corrida")

    lote = generar_aleatorio(100000, SEMILLA)
    tracemalloc.start()
    merge_sort(lote)
    _, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Memoria adicional de merge sort con n=100000: "
          f"{pico / 1024 / 1024:.1f} MB de pico")


def main() -> None:
    """Punto de entrada de la medicion comparativa de la Parte 4."""
    resultados = correr_experimento()
    graficar(resultados, "graficas/parte4_tiempo.png")
    print()
    print("Comprobaciones complementarias citadas en el informe:")
    comprobar_mejor_caso()
    comprobar_cruce_tamanos_pequenos()
    comprobar_merge_sort_grande()


if __name__ == "__main__":
    main()
