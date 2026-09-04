Practica 5 — Modelos Lineales y Correlación. Se intento predecir cuántas repeticiones (Reps) se van a hacer a partir de cuánto peso (Weight) está levantando

1. Revisa la correlación entre Weight y Reps.
2. Entrena un modelo de regresión lineal para predecir Reps a partir de Weight.
3. Calcula qué tan bueno es el modelo (R²).
4. Genera dos gráficas: la línea del modelo sobre los datos, y una gráfica de "residuales" para revisar qué tan bien ajusta.

Antes de llegar al modelo final se probaron otras ideas que no dieron buen resultado. La idea era ver si había una progresión clara (cada vez más peso conforme pasa el tiempo) o si quizás agrupando por día se vería mejor la progresión. Pero el resultado dio que el modelo casi no explica nada (R² = 0.066). El resultado variaba mucho según el ejercicio, sin un patrón consistente.

Se quitaron los registros con peso mayor a 1000 ya que son solo 3 registros de todo el dataset (de máquinas con resistencia acumulada, no peso libre). Al ser casos tan raros y extremos, distorsionaban la línea del modelo sin representar el comportamiento típico del resto de los datos.

El resultado fue: 
- Ecuación del modelo: Reps = 10.49 - 0.0105 × Weight
- R² = 0.149, el modelo explica cerca del 15% de la variación en las repeticiones. Se confirma que existe la relación esperada (a más peso, menos repeticiones), pero también que hay muchos otros factores (qué ejercicio es, la técnica, el cansancio del día) que este modelo no está considerando.
- La relación es negativa: por cada libra adicional de peso, se esperan aproximadamente 0.0105 repeticiones menos.
