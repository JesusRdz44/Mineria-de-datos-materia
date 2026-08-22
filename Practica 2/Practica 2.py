import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# 1. Cargar datos
df = pd.read_csv("../Practica 1/Entrenamiento_gym.csv")
df["Date"] = pd.to_datetime(df["Date"])

print("Filas:", df.shape[0], "| Columnas:", df.shape[1])
print("Rango de fechas:", df["Date"].min().date(), "-", df["Date"].max().date())


# 2. Estadistica descriptiva
num_cols = ["Weight", "Reps", "Distance", "Seconds"]
desc = df[num_cols].describe().T
desc["mediana"] = df[num_cols].median()
desc["moda"] = df[num_cols].mode().iloc[0]
desc["varianza"] = df[num_cols].var()
print("\nEstadística descriptiva:")
print(desc.round(2))

# Ejercicio mas frecuente
print("\nTop 5 ejercicios más registrados:")
print(df["Exercise Name"].value_counts().head(5))

# 3. Entidades y relaciones
# El dataset es una tabla de 3 entidades:
#   SESION (Date, Workout Name) -> EJERCICIO (Exercise Name) -> SERIE (Set Order, Weight, Reps)
# Cada Date identifica una sesión de entrenamiento unica.

fig, ax = plt.subplots(figsize=(9, 3.2))
ax.set_xlim(0, 9)
ax.set_ylim(0, 3)
ax.axis("off")

def entity(x, w, title, attrs, color):
    box = mpatches.FancyBboxPatch((x, 0.4), w, 2.2, boxstyle="round,pad=0.05",
                                   edgecolor="black", facecolor=color, linewidth=1.3)
    ax.add_patch(box)
    ax.text(x + w / 2, 2.35, title, ha="center", fontweight="bold", fontsize=11)
    ax.text(x + w / 2, 1.9, "\n".join(attrs), ha="center", va="top", fontsize=8.5)

entity(0.2, 2.2, "SESIÓN", ["PK: Date", "Workout Name"], "#AED6F1")
entity(3.1, 2.4, "EJERCICIO", ["FK: Date", "Exercise Name"], "#A9DFBF")
entity(6.2, 2.5, "SERIE", ["Set Order, Weight,", "Reps, Distance, Seconds"], "#F9E79F")

ax.annotate("", xy=(3.1, 1.5), xytext=(2.4, 1.5), arrowprops=dict(arrowstyle="->"))
ax.text(2.75, 1.65, "1:N", ha="center", fontsize=8)
ax.annotate("", xy=(6.2, 1.5), xytext=(5.5, 1.5), arrowprops=dict(arrowstyle="->"))
ax.text(5.85, 1.65, "1:N", ha="center", fontsize=8)

ax.set_title("Diagrama Entidad-Relación", fontsize=12, fontweight="bold")
plt.tight_layout()
plt.savefig("diagrama_entidad_relacion.png")
plt.close()

# 4. Métricas de datos agrupados
# Agrupado por ejercicio: promedio de peso y repeticiones
grouped = df.groupby("Exercise Name").agg(
    num_series=("Set Order", "count"),
    peso_promedio=("Weight", "mean"),
    reps_promedio=("Reps", "mean"),
).sort_values("num_series", ascending=False)

print("\nMetricas agrupadas por ejercicio (Top 10 mas registrados):")
print(grouped.head(10).round(1))

# Grafica simple: peso promedio de los 10 ejercicios mas frecuentes
top10 = grouped.head(10)
plt.figure(figsize=(8, 5))
plt.barh(top10.index[::-1], top10["peso_promedio"][::-1], color="#4C72B0")
plt.xlabel("Peso promedio (lb)")
plt.title("Peso promedio por ejercicio (Top 10 más frecuentes)")
plt.tight_layout()
plt.savefig("peso_promedio_por_ejercicio.png")
plt.close()
