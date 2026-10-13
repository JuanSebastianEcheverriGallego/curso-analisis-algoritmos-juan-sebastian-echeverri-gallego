# Retroalimentación — Laboratorio 1: fundamentos, complejidad y recurrencias

**Estudiante:** Juan Sebastián Echeverri Gallego · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-07 23:59 · **Versión revisada:** commit `b41462a`

Excelente trabajo: el informe es completo, está respaldado por sus propias mediciones y el código funciona.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 25 / 25 |
| Calidad de la explicación teórica | 25 / 25 |
| Corrección de la implementación | 20 / 20 |
| Calidad del análisis de las gráficas | 20 / 20 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **99 / 100** |
| **Nota (0–5)** | **4.95** |

## 1. Corrección conceptual (25 / 25)
**Lo que hizo bien:**
- Distingue con claridad entre que el algoritmo sea correcto y que cumpla la ventana de cuatro horas, y nombra esa ventana como la restricción incumplida.
- Explica por qué duplicar la velocidad del servidor no sirve: el trabajo crece con el cuadrado de los datos y la máquina solo da un factor 2.
- Su segundo ejemplo (cruce de facturas y pagos con 45.000 y 52.000 registros, límite de 30 segundos) es propio, concreto y tiene datos y restricción.
- Convierte el tiempo en energía (kWh por noche y por año), identifica dos perjuicios con su responsable del costo y discute la obligación de desempatar de forma explícita y trazable.
- Las dos respuestas respetan el máximo de palabras.

## 2. Calidad de la explicación teórica (25 / 25)
**Lo que hizo bien:**
- Define peor caso, mejor caso y caso promedio indicando sobre qué conjunto se toma cada uno, justifica que usaría el peor caso y deja la predicción escrita antes de medir.
- Plantea la recurrencia de merge sort explicando cada término, la resuelve con árbol de recursión (costo por nivel, número de niveles y total) y la verifica con el método maestro.
- Calcula insertion sort línea a línea y presenta la tabla de complejidades por caso.

## 3. Corrección de la implementación (20 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien, no cambian la lista recibida, cuentan solo comparaciones entre elementos y no usan `sorted()` ni `list.sort()`. La mezcla es propia.
- Los tres generadores dan listas del tamaño pedido, sin repetidos y con semilla reproducible.
- El código cumple PEP 8 y todas las funciones tienen indicaciones de tipo y docstring.

## 4. Calidad del análisis de las gráficas (20 / 20)
**Lo que hizo bien:**
- Las tres gráficas tienen título, ejes con unidades y leyenda, y lo que dice el informe coincide con ellas (por ejemplo, en n = 6400 la curva del escenario C llega a unos 860 ms y la de insertion sort en la Parte 4 a unos 465 ms).
- Identifica con evidencia el peor caso (C), el mejor (B) y el promedio (A), y contrasta con su predicción.
- La conclusión de 4.2 describe lo que hace cada curva y se explica el comportamiento en tamaños pequeños.
- El concepto técnico recomienda merge sort, estima la ventana de cuatro horas declarándola como estimación, responde sobre el servidor con un dato medido y discute la memoria extra y la estabilidad.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- El informe sigue el orden pedido, tiene instrucciones de reproducción, enlaza el código de cada parte y las imágenes se ven con rutas correctas.
- Hay más de cinco commits descriptivos del laboratorio.

**Lo que puede mejorar:**
- No siguió la convención de entrega: publicó en la rama `master` y no en `main`, como se pidió.

## ¿El código funciona?
Sí. Los scripts corren sin errores, ordenan correctamente y generan las tres gráficas. Los conteos de comparaciones se repiten exactamente gracias a la semilla.

## Para el próximo laboratorio
- Publique siempre en la rama `main` (renombre `master` o cree `main` y súbala).
- Elimine del repositorio las carpetas vacías o de relleno que no hacen parte de la entrega.
- Mantenga la práctica de respaldar cada cifra del informe con un script que la reproduzca.
- Siga usando commits pequeños y con mensajes descriptivos.
