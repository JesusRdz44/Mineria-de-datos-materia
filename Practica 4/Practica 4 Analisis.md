Práctica 4. Pruebas Estadísticas
¿El peso que se levanta (Weight) es realmente distinto según el ejercicio? Se comparan los 5 ejercicios más registrados: Squat, Chin Up, Incline Bench Press, Seated Shoulder Press y Weighted dips.

Se revisa si los datos de cada ejercicio siguen una distribución normal. Esto decide qué prueba usar después.
Compara los 5 ejercicios al mismo tiempo para ver si hay alguna diferencia entre ellos.
Compara dos ejercicios específicos para confirmar el resultado a más detalle.
Genera una gráfica para ver la comparación visualmente.

Existen dos pruebas para comparar grupos wque son ANOVA y Kruskal-Wallis. ANOVA solo es válida si los datos de cada grupo tienen una distribución normal. Para decidir una de las dos, se comprobó esto con una prueba llamada Shapiro-Wilk. El resultado fue que ningún ejercicio tiene datos normalizados, así que se usó Kruskal-Wallis, que es la versión que no necesita esa forma específica.

Se revisó solo una muestra de 500 datos por ejercicio ya que con miles de datos, la prueba de normalidad se vuelve demasiado estricta y casi siempre da que no es normal, aunque en la práctica sí lo sea. Tomar una muestra más chica da un resultado más confiable y además permite comparar de forma justa ejercicios que tienen distinta cantidad de registros.

La primera prueba (Kruskal-Wallis) solo dice sí hay diferencia entre los 5 ejercicios en general, pero no dice específicamente cuáles son distintos entre sí. Por eso se agregó una comparación extra, entre los dos ejercicios con más datos.

Resultado:
Sí hay una diferencia real entre los ejercicios (no es casualidad): p < 0.001.
Squat y Chin Up en particular también son claramente distintos entre sí: p < 0.001.
Esto tiene sentido: Squat es un ejercicio de piernas (se levanta más peso) y Chin Up es de tren superior con el propio peso corporal (se levanta mucho menos).
