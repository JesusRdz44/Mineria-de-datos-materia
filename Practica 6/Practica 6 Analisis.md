Practica 6 — Clasificación de Datos (KNN). Pra esta practica se quiere adivinar si una serie de ejercicio fue de pierna o de tren superior, sabiendo solo el peso levantado y las repeticiones hechas. La idea es que los ejercicios de pierna suelen manejar más peso, así que esta información por sí sola podría bastar para distinguirlos.

El dataset no trae esta clasificación. Se construyó revisando el nombre de cada ejercicio (Exercise Name) y buscando palabras como squat, deadlift, leg, etc. Si el nombre contiene alguna de esas palabras, se marca como Pierna; si no, como Tren superior. Asi quedaron:
Pierna: 2,858 series (29%)
Tren superior: 7,074 series (71%)

Separamos los datos en dos partes: 80% para entrenar el modelo y 20% para probarlo, se prueban distintos valores de k para elegir el mejor. Se entrena el modelo final con el mejor k encontrado.
Evalúamos qué tan bien predice, y genera dos gráficas.

Como KNN decide comparando qué tan cerca está un punto de otros, el problema es que Weight llega a valores de cientos y Reps normalmente va de 0 a 20. Sin ajustar la escala, el modelo prácticamente ignoraría Reps porque los números de Weight son mucho más grandes. Se estandarizaron ambas variables para que pesen por igual en la comparación.
Se eligió k=9 porque está justo en el punto donde el modelo ya dejó de mejorar de forma clara y usar un k más grande no mejora mucho, ademas de hacer el modelo más lento sin ganar nada real.

Resultados:
Precisión general: 86%
El modelo es mejor detectando Tren superior (acierta el 95% de las veces que en realidad es tren superior) que Pierna (solo acierta el 64% de las veces que en realidad es pierna).
Como hay ejercicios de pierna con pesos parecidos a los de tren superior (por ejemplo, "Leg curl" no usa tanto peso), lo que hace que el modelo a veces los confunda con tren superior.
