import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv("../Practica 1/Entrenamiento_gym.csv")
print("Filas totales:", df.shape[0])
print("\nMatriz de correlación (Weight, Reps):")
print(df[["Weight", "Reps"]].corr().round(3))
df_modelo = df[df["Weight"] < 1000].copy()
print(f"\nRegistros usados en el modelo: {len(df_modelo)} de {len(df)} "
      f"({len(df) - len(df_modelo)} descartados por Weight >= 1000)")
X = df_modelo[["Weight"]]
y = df_modelo["Reps"]
# Modelo lineal final
modelo = LinearRegression()
modelo.fit(X, y)
predicciones = modelo.predict(X)
r2 = r2_score(y, predicciones)
pendiente = modelo.coef_[0]
intercepto = modelo.intercept_
print("MODELO FINAL: Reps ~ Weight")
print(f"Ecuación: Reps = {intercepto:.2f} + ({pendiente:.4f}) * Weight")
print(f"R^2 = {r2:.4f}")
print(f"Interpretación: por cada libra adicional de peso, las "
      f"repeticiones esperadas bajan en {abs(pendiente):.4f}.")
print(f"El modelo explica {r2*100:.1f}% de la variación en las "
      f"repeticiones; el resto se debe a otros factores (ejercicio "
      f"específico, técnica, fatiga, etc.) no incluidos en este modelo "
      f"simple de una sola variable.")
# Graficas del modelo
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
# 6.1 Dispersión + línea de regresión
axes[0].scatter(df_modelo["Weight"], df_modelo["Reps"], alpha=0.2, s=12)
orden = df_modelo["Weight"].sort_values()
axes[0].plot(orden, modelo.predict(orden.to_frame()), color="red", linewidth=2)
axes[0].set_title(f"Reps ~ Weight (R² = {r2:.3f})")
axes[0].set_xlabel("Weight")
axes[0].set_ylabel("Reps")
# 6.2 Residuales vs valores predichos (para revisar qué tan bien ajusta)
residuos = y - predicciones
axes[1].scatter(predicciones, residuos, alpha=0.2, s=12)
axes[1].axhline(0, color="red", linewidth=2)
axes[1].set_title("Residuales vs. valores predichos")
axes[1].set_xlabel("Reps predichas")
axes[1].set_ylabel("Residual (real - predicho)")
plt.tight_layout()
plt.savefig("modelo_lineal_reps_weight.png")
plt.close()
