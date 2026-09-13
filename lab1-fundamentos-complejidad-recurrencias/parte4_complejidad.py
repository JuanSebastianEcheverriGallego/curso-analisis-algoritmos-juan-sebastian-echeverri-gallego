"""Medicion comparativa de la Parte 4: insertion sort contra merge sort.

Los dos algoritmos se ejecutan sobre el escenario A de Tamiza (lote en
orden aleatorio), con los mismos tamanos de entrada de la Parte 3, y se
grafica el tiempo de ejecucion de cada uno en los mismos ejes.
"""

import time
from statistics import median

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio

TAMANIOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3
SEMILLA = 42

ALGORITMOS = [
    ("Insertion sort", insertion_sort, "#0072B2", "o"),
    ("Merge sort", merge_sort, "#D55E00", "s"),
]


def medir(algoritmo, lote: list[int]) -> tuple[float, int]:
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


def main() -> None:
    """Punto de entrada de la medicion comparativa de la Parte 4."""
    resultados = correr_experimento()
    graficar(resultados, "graficas/parte4_tiempo.png")


if __name__ == "__main__":
    main()
