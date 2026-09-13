"""Experimento de la Parte 3: peor, mejor y caso promedio de insertion sort.

Ejecuta insertion_sort sobre los tres escenarios de entrada de Tamiza,
registra el numero de comparaciones y el tiempo de ejecucion, y guarda
las dos graficas de la carpeta graficas/.
"""

import time
from statistics import median

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso

TAMANIOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3
SEMILLA = 42

ESCENARIOS = [
    ("A - Aleatorio", generar_aleatorio, "#0072B2", "o"),
    ("B - Casi ordenado", generar_casi_ordenado, "#D55E00", "s"),
    ("C - Orden inverso", generar_inverso, "#009E73", "^"),
]


def generar_lote(generador, n: int) -> list[int]:
    """Construye el lote de un escenario respetando la firma del generador.

    Args:
        generador: funcion generadora del escenario.
        n: cantidad de registros del lote.

    Returns:
        Lista de n indices de riesgo del escenario correspondiente.
    """
    if generador is generar_inverso:
        return generador(n)
    return generador(n, SEMILLA)


def medir(lote: list[int]) -> tuple[float, int]:
    """Mide el tiempo de insertion_sort sobre un lote ya construido.

    El lote se genera antes de llamar a esta funcion para que el
    cronometro solo cubra la ejecucion del algoritmo.

    Args:
        lote: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con el tiempo mediano en milisegundos de
        REPETICIONES corridas y el numero de comparaciones.
    """
    tiempos = []
    comparaciones = 0
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        _, comparaciones = insertion_sort(lote)
        fin = time.perf_counter()
        tiempos.append((fin - inicio) * 1000)
    return median(tiempos), comparaciones


def correr_experimento() -> dict[str, dict[str, list[float]]]:
    """Ejecuta la medicion de los tres escenarios en todos los tamanos.

    Returns:
        Diccionario con el nombre del escenario como clave y, como
        valor, las listas de tiempos y comparaciones medidos.
    """
    resultados = {}
    for nombre, generador, _, _ in ESCENARIOS:
        tiempos = []
        comparaciones = []
        for n in TAMANIOS:
            lote = generar_lote(generador, n)
            tiempo, comps = medir(lote)
            tiempos.append(tiempo)
            comparaciones.append(comps)
            print(f"{nombre:20s} n={n:5d} {comps:12d} comp "
                  f"{tiempo:9.2f} ms")
        resultados[nombre] = {"tiempo": tiempos,
                              "comparaciones": comparaciones}
    return resultados


def graficar(resultados: dict, clave: str, titulo: str, eje_y: str,
             archivo: str) -> None:
    """Dibuja una metrica de los tres escenarios en los mismos ejes.

    Args:
        resultados: salida de correr_experimento().
        clave: metrica a graficar ("tiempo" o "comparaciones").
        titulo: titulo de la grafica.
        eje_y: rotulo del eje vertical con su unidad.
        archivo: ruta del archivo PNG de salida.
    """
    figura, ejes = plt.subplots(figsize=(8, 5))
    for nombre, _, color, marca in ESCENARIOS:
        ejes.plot(TAMANIOS, resultados[nombre][clave], marker=marca,
                  markersize=8, linewidth=2, color=color, label=nombre)
    ejes.set_title(titulo)
    ejes.set_xlabel("Tamaño de entrada n (número de registros)")
    ejes.set_ylabel(eje_y)
    ejes.grid(True, linewidth=0.5, alpha=0.4)
    ejes.legend(title="Escenario de entrada")
    figura.tight_layout()
    figura.savefig(archivo, dpi=150)
    plt.close(figura)
    print(f"Grafica guardada en {archivo}")


def main() -> None:
    """Punto de entrada del experimento de la Parte 3."""
    resultados = correr_experimento()
    graficar(resultados, "comparaciones",
             "Insertion sort: comparaciones vs. tamaño de entrada",
             "Comparaciones entre elementos (unidades)",
             "graficas/parte3_comparaciones.png")
    graficar(resultados, "tiempo",
             "Insertion sort: tiempo de ejecución vs. tamaño de entrada",
             "Tiempo de ejecución (milisegundos)",
             "graficas/parte3_tiempo.png")


if __name__ == "__main__":
    main()
