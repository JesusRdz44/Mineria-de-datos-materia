Practica 2. Estadistica Descriptiva
Dataset: Entrenamiento_gym.csv (registro de entrenamientos de gimnasio)

Calcula estadistica descriptiva (media, mediana, moda, desviacion estandar, varianza) de las variables numericas Weight, Reps, Distance y Seconds
Identifica las entidades y relaciones implicitas en el dataset y genera su diagrama entidad-relacion
Calcula metricas agrupadas por Exercise Name (numero de series, peso promedio, repeticiones promedio)

Distance y Seconds en 0: No se trataron como valores faltantes ni se imputaron. El dataset es predominantemente de ejercicios de fuerza (peso x repeticiones), no de cardio, por lo que un valor de 0 en estas columnas es informativo ("no aplica a este ejercicio"), no un dato ausente
Identificación de entidades (Sesión → Ejercicio → Serie): Se verifico que la columna Date identifica de forma unica una sesión de entrenamiento: el numero de fechas unicas (583) coincide exactamente con el numero de combinaciones unicas de (Date, Workout Name). Esto confirma la relación 1:N entre Sesión y Ejercicio, y entre Ejercicio y Serie (a través de Set Order)
Metrica elegida para agrupar (peso promedio por ejercicio): Se uso peso promedio en vez de peso maximo porque el maximo es sensible a valores atipicos de una sola sesión (ej. un intento aislado de una repetición muy pesada), mientras que el promedio refleja mejor la carga habitual manejada en cada ejercicio
