import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("../Practica 1/Entrenamiento_gym.csv")
df["Date"] = pd.to_datetime(df["Date"])
print("Filas:", df.shape[0], "| Columnas:", df.shape[1])

def plot_histograma(data, columna, bins, titulo, archivo):
    plt.figure(figsize=(8, 5))
    plt.hist(data[columna], bins=bins, edgecolor="black")
    plt.title(titulo)
    plt.xlabel(columna)
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.savefig(archivo)
    plt.close()
  
def plot_boxplot(data, columna, agrupar_por, categorias, titulo, archivo):
    grupos = [data[data[agrupar_por] == cat][columna] for cat in categorias]
    plt.figure(figsize=(9, 5))
    plt.boxplot(grupos, tick_labels=categorias, patch_artist=True)
    plt.title(titulo)
    plt.ylabel(columna)
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(archivo)
    plt.close()

def plot_dispersion(data, col_x, col_y, titulo, archivo):
    plt.figure(figsize=(8, 5))
    plt.scatter(data[col_x], data[col_y], alpha=0.3, s=15)
    plt.title(titulo)
    plt.xlabel(col_x)
    plt.ylabel(col_y)
    plt.tight_layout()
    plt.savefig(archivo)
    plt.close()

def plot_pastel(data, columna, top_n, titulo, archivo):
    conteo = data[columna].value_counts()
    top = conteo.head(top_n)
    otros = conteo.iloc[top_n:].sum()
    valores = list(top.values) + [otros]
    etiquetas = list(top.index) + ["Otros"]
    plt.figure(figsize=(7, 7))
    plt.pie(valores, labels=etiquetas, autopct="%1.1f%%", startangle=90)
    plt.title(titulo)
    plt.tight_layout()
    plt.savefig(archivo)
    plt.close()

def plot_barras(data, columna, top_n, titulo, archivo):
    conteo = data[columna].value_counts().head(top_n)
    plt.figure(figsize=(8, 5))
    plt.barh(conteo.index[::-1], conteo.values[::-1])
    plt.title(titulo)
    plt.xlabel("Número de series registradas")
    plt.tight_layout()
    plt.savefig(archivo)
    plt.close()

plot_histograma(df, "Weight", bins=30,titulo="Distribución del peso levantado (Weight)",archivo="01_histograma_weight.png",)
top5_ejercicios = df["Exercise Name"].value_counts().head(5).index.tolist()
plot_boxplot(df, "Weight", agrupar_por="Exercise Name", categorias=top5_ejercicios,titulo="Distribución de peso por ejercicio (Top 5 más frecuentes)",archivo="02_boxplot_weight_por_ejercicio.png",)
plot_dispersion(df, "Weight", "Reps",titulo="Relación entre peso (Weight) y repeticiones (Reps)",archivo="03_dispersion_weight_reps.png",)
plot_pastel(df, "Workout Name", top_n=6,titulo="Proporción de series por tipo de rutina (Top 6 + Otros)",archivo="04_pastel_workout_name.png",)
plot_barras(df, "Exercise Name", top_n=10,titulo="Top 10 ejercicios más registrados",archivo="05_barras_top_ejercicios.png",)
