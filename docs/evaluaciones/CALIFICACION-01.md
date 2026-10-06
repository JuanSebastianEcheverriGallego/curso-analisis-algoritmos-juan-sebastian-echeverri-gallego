# Retroalimentación — Fundamentos, complejidad y recurrencias

**Estudiante:** Juan Sebastián Echeverri Gallego · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `f76763e`

Excelente trabajo: un informe sólido, con datos propios y razonamientos bien apoyados.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 25 / 25 |
| Calidad de la explicación teórica | 25 / 25 |
| Corrección de la implementación | 18 / 20 |
| Calidad del análisis de las gráficas | 19 / 20 |
| Documentación y organización del informe | 7 / 10 |
| **Total** | **94 / 100** |
| **Nota (0–5)** | **4.70** |

## 1. Corrección conceptual (25 / 25)
**Lo que hizo bien:**
- Distingue con claridad corrección y eficiencia, y nombra la restricción que se incumple: la ventana de cuatro horas.
- Explica que duplicar el servidor solo divide el tiempo entre dos, mientras el trabajo creció unas 3.600 veces.
- Su segundo ejemplo (conciliación de facturas contra pagos) tiene datos, cantidad de registros y la restricción incumplida.
- En la parte ambiental calcula el consumo de energía por noche y por año.
- Identifica dos perjuicios concretos (el paciente y el operador del centro de contacto) y dice quién asume el costo de cada uno.
- Discute muy bien la obligación de que el desempate sea estable y trazable.

## 2. Calidad de la explicación teórica (25 / 25)
**Lo que hizo bien:**
- Define peor caso, mejor caso y caso promedio indicando sobre qué conjunto de entradas se toma cada uno, y justifica por qué usaría el peor caso.
- Dejó escrita la predicción antes de medir y luego la contrastó con los resultados.
- Plantea la recurrencia de merge sort explicando cada término y la resuelve con árbol de recursión paso a paso, con verificación por método maestro.
- El análisis línea a línea de insertion sort y la tabla de complejidades están completos.

## 3. Corrección de la implementación (18 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien, no cambian la lista recibida, cuentan comparaciones entre elementos y no usan `sorted()` ni `list.sort()`.
- `merge_sort` tiene su propia mezcla recursiva.
- Los tres generadores producen lotes del tamaño pedido, con valores distintos y semilla reproducible.
- El código cumple PEP 8 y casi todas las funciones tienen docstring estilo Google.

**Lo que puede mejorar:**
- Algunos parámetros de las funciones auxiliares (`generador` en `generar_lote`, `algoritmo` en `medir`) no tienen indicación de tipo, y el tipo de `resultados` en `graficar` quedó incompleto.

## 4. Calidad del análisis de las gráficas (19 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes rotulados con unidades y leyenda, y las curvas están en los mismos ejes.
- Identifica con cifras el peor caso (C), el mejor (B) y el cercano al promedio (A), y compara con las fórmulas teóricas.
- Concluye que merge sort es mejor leyendo lo que hace cada curva, y explica el comportamiento en tamaños pequeños.
- El concepto técnico recomienda un algoritmo, responde a la propuesta del servidor con un dato medido y declara la extrapolación como estimación.

**Lo que puede mejorar:**
- Cita mediciones (uso de memoria, prueba con 200.000 registros, cruce cerca de n = 60) que no salen de los scripts entregados, así que el profesor no puede reproducirlas. Incluya ese código o explique cómo las obtuvo.

## 5. Documentación y organización del informe (7 / 10)
**Lo que hizo bien:**
- Estructura de carpetas, archivos y gráficas tal como pide el entregable; las imágenes se ven con ruta relativa.
- Instrucciones de reproducción claras y enlaces al código en cada parte práctica.

**Lo que puede mejorar:**
- No siguió la convención de entrega: el trabajo está en la rama `master` y no en `main`.
- Los seis commits del laboratorio se hicieron todos en menos de dos minutos, así que no muestran el avance real del trabajo. Haga commits a medida que avanza.

## ¿El código funciona?
Sí. Los scripts corren sin errores, los algoritmos ordenan bien en mis pruebas y se generan las tres gráficas. Los conteos de comparaciones coinciden con los de su informe.

## Para el próximo laboratorio
- Suba el trabajo a la rama `main`.
- Haga commits pequeños y espaciados mientras trabaja.
- Ponga indicaciones de tipo en todos los parámetros, también en las funciones auxiliares.
- Si cita una medición en el informe, incluya el código que la produce.
