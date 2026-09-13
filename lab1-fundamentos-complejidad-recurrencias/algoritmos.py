"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    lista = list(datos)
    comparaciones = 0
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0:
            comparaciones += 1
            if lista[j] < clave:
                lista[j + 1] = lista[j]
                j -= 1
            else:
                break
        lista[j + 1] = clave
    return lista, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    lista = list(datos)
    if len(lista) <= 1:
        return lista, 0
    medio = len(lista) // 2
    izquierda, comp_izq = merge_sort(lista[:medio])
    derecha, comp_der = merge_sort(lista[medio:])
    mezclada, comp_mezcla = mezclar(izquierda, derecha)
    return mezclada, comp_izq + comp_der + comp_mezcla


def mezclar(izquierda: list[int], derecha: list[int]) -> tuple[list[int], int]:
    """Combina dos listas ya ordenadas de mayor a menor en una sola.

    Args:
        izquierda: primera mitad, ordenada de mayor a menor.
        derecha: segunda mitad, ordenada de mayor a menor.

    Returns:
        Una tupla con la lista combinada y el numero de comparaciones
        entre elementos realizadas en la mezcla.
    """
    resultado = []
    comparaciones = 0
    i = 0
    j = 0
    while i < len(izquierda) and j < len(derecha):
        comparaciones += 1
        if izquierda[i] >= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado, comparaciones
