import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

df = pd.read_csv("../Practica 1/Entrenamiento_gym.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Volume"] = df["Weight"] * df["Reps"] 
df["Anio"] = df["Date"].dt.year
df["Mes"] = df["Date"].dt.to_period("M")

# correlación y regresión (constancia vs. volumen mensual)

mensual = df.groupby("Mes").agg(sesiones=("Date", "nunique"), volumen=("Volume", "sum"))
mensual["vol_por_sesion"] = mensual["volumen"] / mensual["sesiones"]

# Los datos empiezan el 23 de octubre de 2015, así que ese primer mes está incompleto y se deja fuera de la comparación
completos = mensual.iloc[1:]
r, p = stats.pearsonr(completos["sesiones"], completos["volumen"])
r_vps = np.corrcoef(completos["vol_por_sesion"], completos["sesiones"])[0, 1]
reg = stats.linregress(completos["sesiones"], completos["volumen"])

print("1. Constancia vs. volumen mensual")
print(f"Meses analizados: {len(completos)} (sin oct-2015, mes incompleto)")
print(f"Correlación sesiones-volumen: r = {r:.3f} (R2 = {r**2:.3f}, p = {p:.1e})")
print(f"Cada sesión extra al mes suma ~{reg.slope:,.0f} de volumen")
print(f"Correlación volumen por sesión vs. sesiones: r = {r_vps:.3f}")

lv = np.log(completos["volumen"])
parte_sesiones = np.cov(lv, np.log(completos["sesiones"]))[0, 1] / lv.var()
parte_tamano = np.cov(lv, np.log(completos["vol_por_sesion"]))[0, 1] / lv.var()
print(f"De la variación del volumen mensual: {parte_sesiones * 100:.0f}% viene de " f"cuántas sesiones se hacen y {parte_tamano * 100:.0f}% de cuánto se hace " f"en cada sesión")

plt.figure(figsize=(9, 5.5))
plt.scatter(completos["sesiones"], completos["volumen"], s=55, alpha=0.8)
x = np.array([completos["sesiones"].min(), completos["sesiones"].max()])
plt.plot(x, reg.intercept + reg.slope * x, color="red", linewidth=2)
plt.title(f"Más sesiones al mes, más volumen (r = {r:.2f}, R² = {r**2:.2f})")
plt.xlabel("Sesiones de entrenamiento en el mes")
plt.ylabel("Volumen mensual (peso x repeticiones)")
plt.tight_layout()
plt.savefig("01_constancia_vs_volumen.png", dpi=200)
plt.close()

# clustering (mezcla de tipos de series por año). K-Means con k=3 sobre Weight y Reps
series = df[df["Weight"] < 1000].copy()
X = StandardScaler().fit_transform(series[["Weight", "Reps"]])
series["cluster"] = KMeans(n_clusters=3, random_state=42, n_init=10).fit_predict(X)
silhouette = silhouette_score(X, series["cluster"])

# Se nombra cada grupo según su peso promedio (de menor a mayor)
orden = series.groupby("cluster")["Weight"].mean().sort_values().index
nombres = dict(zip(orden, ["Ligeras", "Fuerza pesada", "Peso muy alto"]))
series["tipo"] = series["cluster"].map(nombres)

mezcla = pd.crosstab(series["Anio"], series["tipo"], normalize="index") * 100
mezcla = mezcla[["Ligeras", "Fuerza pesada", "Peso muy alto"]]

series_por_sesion = df.groupby(["Anio", "Date"]).size().groupby("Anio").mean()
squat = df[df["Exercise Name"] == "Squat (Barbell)"]
squat_mediana = squat.groupby("Anio")["Weight"].median()

print(f"\n2. Clustering K-Means (k=3, silhouette = {silhouette:.2f})")
print("Mezcla de series por año (% de las series):")
print(mezcla.round(1))
print("\nSeries por sesión (promedio por año):")
print(series_por_sesion.round(1))
print("\nPeso mediano en Squat (Barbell) por año:")
print(squat_mediana)
print(f"Cambio 2015 -> 2018: {squat_mediana[2015]:.0f} -> {squat_mediana[2018]:.0f} lb " f"({(squat_mediana[2018] / squat_mediana[2015] - 1) * 100:+.0f}%)")

fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
mezcla.plot(kind="bar", stacked=True, ax=axes[0], rot=0,
            color=["#9ecae1", "#2171b5", "#08306b"])
axes[0].set_title("Cada año, más series de fuerza pesada")
axes[0].set_xlabel("")
axes[0].set_ylabel("% de las series del año")
axes[0].legend(title="Tipo de serie", fontsize=10, loc="upper center",
               bbox_to_anchor=(0.5, -0.08), ncol=3)
axes[1].bar(series_por_sesion.index.astype(str), series_por_sesion.values,color="#2171b5")
axes[1].set_title(" y sesiones cada vez más cortas")
axes[1].set_ylabel("Series por sesión")
axes[1].set_ylim(0, 31)
for i, v in enumerate(series_por_sesion.values):
    axes[1].text(i, v + 0.4, f"{v:.0f}", ha="center")
plt.tight_layout()
plt.savefig("02_mezcla_series_por_anio.png", dpi=200)
plt.close()

# pronóstico (promedio de los últimos 3 meses)
y = mensual["volumen"].values.astype(float)
errores = [abs(y[i] - y[i - 3:i].mean()) for i in range(18, len(y))]
mae = np.mean(errores)
prediccion = y[-3:].mean()
sesiones_recientes = mensual["sesiones"].tail(3).mean()

print("\n3. Pronóstico oct 2018 - mar 2019")
print(f"Volumen mensual esperado: {prediccion:,.0f}")
print(f"Error promedio del modelo (MAE): {mae:,.0f} ({mae / y.mean() * 100:.0f}% del promedio)")
print(f"Rango: {prediccion - mae:,.0f} a {prediccion + mae:,.0f}")
print(f"Sesiones al mes en los últimos 3 meses: {sesiones_recientes:.1f}")

fechas = mensual.index.to_timestamp()
futuro = pd.period_range(mensual.index[-1] + 1, periods=6, freq="M").to_timestamp()
poco = completos[completos["sesiones"] <= 6]   # meses con muy pocas sesiones
pocas = mensual.index.isin(poco.index)

print("\nMeses con 6 sesiones o menos")
print(poco[["sesiones", "volumen"]])
print(f"Volumen promedio de esos meses: {poco['volumen'].mean():,.0f}")
print(f"Volumen promedio del resto: {completos[completos['sesiones'] > 6]['volumen'].mean():,.0f}")
print("\nMeses con 15 sesiones o más, por año:")
print((completos["sesiones"] >= 15).groupby(completos.index.year).agg(["sum", "count"]))

plt.figure(figsize=(11, 5.5))
plt.plot(fechas, y, marker="o", label="Volumen real")
plt.scatter(fechas[pocas], y[pocas], color="red", s=110, zorder=3, label="Mes con 6 sesiones o menos")
plt.plot(futuro, [prediccion] * 6, marker="o", linestyle="--", label="Pronóstico")
plt.fill_between(futuro, prediccion - mae, prediccion + mae, alpha=0.2)
plt.title("Los baches de volumen coinciden con meses de pocas sesiones")
plt.xlabel("Mes")
plt.ylabel("Volumen mensual")
plt.legend(fontsize=11)
plt.tight_layout()
plt.savefig("03_pronostico_volumen.png", dpi=200)
plt.close()
