Práctica 4.Pruebas Estadísticas

¿El peso levantado (Weight) difiere significativamente entre distintos ejercicios? Se comparan los 5 ejercicios con más series registradas: Squat (Barbell), Chin Up, Incline Bench Press (Barbell), Seated Shoulder Press (Barbell) y Weighted dips.

1. Prueba de normalidad por grupo, para decidir entre ANOVA o Kruskal-Wallis
2. Prueba de diferencia entre los 5 grupos (Kruskal-Wallis, según el resultado del paso 1).
3. Comparación específica entre los dos ejercicios con más registros (Mann-Whitney U), como profundización sobre el resultado general.
4. Boxplot comparativo con el resultado de la prueba en el título.

ANOVA asume que los datos de cada grupo siguen una distribución normal. En vez de asumir esto o elegir Kruskal-Wallis, se corrió Shapiro-Wilk sobre cada uno de los 5 grupos. El resultado es que ninguno de los 5 ejercicios pasa la prueba de normalidad (p < 0.0001 en todos), por lo que se descarta ANOVA y se usa Kruskal-Wallis, que compara las distribuciones mediante rangos en vez de medias.

Shapiro-Wilk pierde potencia estadística con muestras muy grandes ya que casi cualquier desviación mínima de la normalidad resulta significativa. Se tomó una muestra aleatoria de 500 observaciones por grupo (o el total si el grupo tiene menos) para mantener la prueba comparable entre ejercicios con tamaños de muestra muy distintos.

Resultados
- Kruskal-Wallis: H = 3650.43, p < 0.001. Existe diferencia significativa en el peso levantado entre al menos un par de los 5 ejercicios comparados.
- Mann-Whitney (Squat vs. Chin Up): p < 0.001 estos dos ejercicios en particular tienen distribuciones de peso significativamente distintas, consistente con que son movimientos de piernas vs. tren superior con cargas típicas muy diferentes
