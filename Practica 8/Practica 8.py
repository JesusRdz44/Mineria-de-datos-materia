import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("../Practica 1/Entrenamiento_gym.csv")
df["Date"] = pd.to_datetime(df["Date"])

#  mide cuanto trabajo total se hizo en cada serie
df["Volume"] = df["Weight"] * df["Reps"]

# Se agrupa por mes para tener una observacion por mes
serie = df.groupby(df["Date"].dt.to_period("M"))["Volume"].sum()
y = serie.values.astype(float)
print(f"Meses en la serie: {len(y)} ({serie.index[0]} a {serie.index[-1]})")

# Para cada mes desde el 18 en adelante, el modelo predice ese mes con el promedio de los 3 meses anteriores, y se compara contra lo que realmente pasa
errores = [abs(y[i] - y[i - 3:i].mean()) for i in range(18, len(y))]
mae = np.mean(errores)
print(f"Error promedio del modelo (MAE): {mae:,.0f} "
      f"({mae / y.mean() * 100:.0f}% del volumen mensual promedio)")

prediccion = y[-3:].mean()
meses_futuros = pd.period_range(serie.index[-1] + 1, periods=6, freq="M")

print(f"\nPronóstico mensual (oct 2018 - mar 2019): {prediccion:,.0f}")
print(f"Rango esperado de error promedio): {prediccion - mae:,.0f} a "
      f"{prediccion + mae:,.0f}")

fechas = serie.index.to_timestamp()
fechas_fut = meses_futuros.to_timestamp()

plt.figure(figsize=(11, 5))
plt.plot(fechas, y, marker="o", label="Volumen real")
plt.plot(fechas_fut, [prediccion] * 6, marker="o", linestyle="--",
         label="Pronóstico")
plt.fill_between(fechas_fut, prediccion - mae, prediccion + mae, alpha=0.2,
                 label="Rango de error")
plt.title("Volumen mensual de entrenamiento y pronóstico a 6 meses")
plt.xlabel("Mes")
plt.ylabel("Volumen (Weight x Reps)")
plt.legend()
plt.tight_layout()
plt.savefig("pronostico_volumen.png")
plt.close()
