import re
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_csv("../Practica 1/Entrenamiento_gym.csv")
print("Comentarios en Notes:", df["Notes"].notna().sum())
print("Comentarios en Workout Notes:", df["Workout Notes"].notna().sum())

# Palabras que no aportan informacion como conectores, simbolos sueltos y palabras genericas de las rutinas
palabras_vacias = {"with", "x", "up", "day", "workout"}

# Se juntan singular y plural para que no cuenten como palabras distintas
singular = {"squats": "squat", "chins": "chin", "legs": "leg",
            "shoulders": "shoulder", "rows": "row", "pulls": "pull",
            "dumbbells": "dumbbell"}

def limpiar(texto):
    palabras = re.findall(r"[a-z]+", texto.lower().replace("t-bar", "tbar"))
    palabras = [singular.get(p, p) for p in palabras]
    return [p for p in palabras if p not in palabras_vacias]

def contar_palabras(serie_texto):
    conteo = Counter()
    for texto in serie_texto:
        conteo.update(limpiar(texto))
    return conteo

frec_ejercicios = contar_palabras(df["Exercise Name"])
frec_rutinas = contar_palabras(df["Workout Name"])

print("\nTop 10 palabras en nombres de ejercicios:")
for palabra, n in frec_ejercicios.most_common(10):
    print(f"  {palabra:12s} {n}")

print("\nTop 10 palabras en nombres de rutinas:")
for palabra, n in frec_rutinas.most_common(10):
    print(f"  {palabra:12s} {n}")

# Pares de palabras seguidas como bench press
pares = Counter()
for texto in df["Exercise Name"]:
    palabras = limpiar(texto)
    pares.update(zip(palabras, palabras[1:]))

print("\nTop 10 pares de palabras en ejercicios:")
for (a, b), n in pares.most_common(10):
    print(f"  {a} {b:12s} {n}")

# Equipo usado
total = len(df)
print("\nSeries segun el equipo mencionado en el nombre del ejercicio:")
for equipo in ["barbell", "dumbbell", "cable"]:
    n = frec_ejercicios[equipo]
    print(f"  {equipo:10s} {n:5d} series ({n / total * 100:.1f}%)")

# Estilo de entrenamiento mencionado en el nombre de la rutina
print("\nRutinas que mencionan 'heavy' (pesado) vs 'light' (ligero):")
print(f"  heavy: {frec_rutinas['heavy']} series | light: {frec_rutinas['light']} series")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
for eje, frec, titulo in [(axes[0], frec_ejercicios, "Nombres de ejercicios"),
                          (axes[1], frec_rutinas, "Nombres de rutinas")]:
    nube = WordCloud(width=700, height=500, background_color="white")
    nube.generate_from_frequencies(frec)
    eje.imshow(nube, interpolation="bilinear")
    eje.set_title(titulo)
    eje.axis("off")

plt.tight_layout()
plt.savefig("nube_de_palabras.png")
plt.close()

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
for eje, frec, titulo in [(axes[0], frec_ejercicios, "Ejercicios"),
                          (axes[1], frec_rutinas, "Rutinas")]:
    top = frec.most_common(10)
    eje.barh([p for p, _ in top][::-1], [n for _, n in top][::-1])
    eje.set_title(f"Top 10 palabras en nombres de {titulo.lower()}")
    eje.set_xlabel("Series")

plt.tight_layout()
plt.savefig("frecuencia_palabras.png")
plt.close()
