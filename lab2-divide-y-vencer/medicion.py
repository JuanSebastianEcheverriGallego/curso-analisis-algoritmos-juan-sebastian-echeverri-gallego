"""Medicion comparativa: fuerza bruta contra divide y venceras.

Mide el tiempo de ejecucion de las dos soluciones del subarreglo maximo
sobre la misma serie de variaciones de caja, para varios tamanos de
entrada, y guarda la grafica en graficas/tiempo_vs_n.png.
"""

import random
import time
from collections.abc import Callable
from statistics import median

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

TAMANOS = [10, 20, 30, 40, 50, 100, 500, 1000, 2000, 4000, 8000, 16000]
REPETICIONES = 7
SEMILLA = 42


def generar_serie(n: int, semilla: int = SEMILLA) -> list[int]:
    """Genera la variacion diaria de caja de una tienda.

    Args:
        n: cantidad de dias de la serie.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.

    Returns:
        Lista de n variaciones enteras entre -100 y 100.
    """
    generador = random.Random(semilla)
    return [generador.randint(-100, 100) for _ in range(n)]


def medir(
    funcion: Callable[..., tuple[int, int, float]], *argumentos: object
) -> tuple[float, tuple[int, int, float]]:
    """Cronometra una de las dos soluciones sobre una serie ya generada.

    La serie se construye antes de llamar a esta funcion para que el
    cronometro cubra unicamente la llamada al algoritmo.

    Args:
        funcion: solucion a medir.
        *argumentos: argumentos con los que se llama la solucion.

    Returns:
        Una tupla con el tiempo mediano en milisegundos de REPETICIONES
        corridas y el resultado (inicio, fin, suma) del algoritmo.
    """
    tiempos = []
    resultado = None
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        resultado = funcion(*argumentos)
        fin = time.perf_counter()
        tiempos.append((fin - inicio) * 1000)
    return median(tiempos), resultado


def correr_experimento() -> tuple[list[float], list[float]]:
    """Mide las dos soluciones sobre la misma serie en cada tamano.

    Returns:
        Una tupla con la lista de tiempos de fuerza bruta y la lista de
        tiempos de divide y venceras, en milisegundos.
    """
    tiempos_bruta = []
    tiempos_dyv = []
    for n in TAMANOS:
        serie = generar_serie(n)
        tiempo_bruta, resultado_bruta = medir(subarreglo_fuerza_bruta, serie)
        tiempo_dyv, resultado_dyv = medir(subarreglo_maximo, serie, 0, n - 1)

        # Las dos soluciones deben encontrar la misma mejor racha.
        assert resultado_bruta[2] == resultado_dyv[2], (
            f"n={n}: fuerza bruta dio {resultado_bruta[2]} y divide y "
            f"venceras dio {resultado_dyv[2]}")

        tiempos_bruta.append(tiempo_bruta)
        tiempos_dyv.append(tiempo_dyv)
        print(f"n={n:6d}  suma={resultado_bruta[2]:9.0f}  "
              f"bruta={tiempo_bruta:10.4f} ms  dyv={tiempo_dyv:8.4f} ms")
    return tiempos_bruta, tiempos_dyv


def graficar(tiempos_bruta: list[float], tiempos_dyv: list[float],
             archivo: str) -> None:
    """Dibuja el tiempo de las dos soluciones en los mismos ejes.

    Args:
        tiempos_bruta: tiempos de fuerza bruta en milisegundos.
        tiempos_dyv: tiempos de divide y venceras en milisegundos.
        archivo: ruta del archivo PNG de salida.
    """
    figura, ejes = plt.subplots(figsize=(8, 5))
    ejes.plot(TAMANOS, tiempos_bruta, marker="o", markersize=8, linewidth=2,
              color="#0072B2", label="Fuerza bruta")
    ejes.plot(TAMANOS, tiempos_dyv, marker="s", markersize=8, linewidth=2,
              color="#D55E00", label="Divide y vencerás")
    ejes.set_title("Subarreglo máximo: tiempo de ejecución vs. tamaño de "
                   "la serie")
    ejes.set_xlabel("Tamaño de la serie n (número de días)")
    ejes.set_ylabel("Tiempo de ejecución (milisegundos)")
    ejes.grid(True, linewidth=0.5, alpha=0.4)
    ejes.legend(title="Algoritmo")
    figura.tight_layout()
    figura.savefig(archivo, dpi=150)
    plt.close(figura)
    print(f"Grafica guardada en {archivo}")


def main() -> None:
    """Punto de entrada de la medicion."""
    tiempos_bruta, tiempos_dyv = correr_experimento()
    graficar(tiempos_bruta, tiempos_dyv, "graficas/tiempo_vs_n.png")


if __name__ == "__main__":
    main()
