Practica 7 — Agrupamiento de Datos

Sin decirle nada al modelo se quiere ver si existen grupos de series de entrenamiento según el peso levantado y las repeticiones hechas, a diferencia de la práctica 6 , aquí el modelo descubre los grupos por sí solo

Como K-Means agrupa según qué tan cerca están los puntos entre sí, Weight llega a cientos y Reps normalmente no pasa de 20, sin ajustar la escala el modelo solo tomaría en cuenta el peso e ignoraría las repeticiones

Se probaron valores de k del 2 al 8 y se midió el que tan bien separados quedan los grupos (más alto es mejor). El mejor resultado fue con k=3

El resultado fue:
3 grupos naturales:

Grupo 1: 94 peso promedio, 10.6 repeticiones promedio, 5,245 cantidad de series, Series ligeras de alto volumen
Grupo 2: 241 peso promedio, 6.2 repeticiones promedio, 4,371 cantidad de series , Series de fuerza pesada: bastante peso, pocas repeticiones
Grupo 3: 498 peso promedio, 10.8 repeticiones promedio, 313 cantidad de series, Peso muy alto con muchas repeticiones, probablemente ejercicios de pierna o maquina que permiten mover más peso

Aunque el grupo 3 sea el más pequeño (solo 3% de las series), representa un patrón distinto: no sigue la relación típica de más peso, menos repeticiones que sí se ve entre los grupos 1 y 2
