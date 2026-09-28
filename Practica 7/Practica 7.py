import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

df = pd.read_csv("../Practica 1/Entrenamiento_gym.csv")

df = df[df["Weight"] < 1000].copy()
print(f"Registros usados: {len(df)}")
X = df[["Weight", "Reps"]]
# K-Means agrupa segun distancias, asi que las variables deben estar en la misma escala
scaler = StandardScaler()
X_esc = scaler.fit_transform(X)
mejor_k = 3

modelo = KMeans(n_clusters=mejor_k, random_state=42, n_init=10)
df["cluster"] = modelo.fit_predict(X_esc)
silhouette_final = silhouette_score(X_esc, df["cluster"])

print(f"Modelo K-Means (k={mejor_k})")
print(f"Silhouette score: {silhouette_final:.4f}")

print("\nCaracterísticas de cada grupo encontrado:")
resumen = df.groupby("cluster")[["Weight", "Reps"]].mean().round(1)
resumen["num_series"] = df.groupby("cluster").size()
print(resumen)

plt.figure(figsize=(7, 5))
scatter = plt.scatter(df["Weight"], df["Reps"], c=df["cluster"],
                       cmap="viridis", alpha=0.4, s=12)
plt.title(f"Grupos encontrados por K-Means (k={mejor_k})")
plt.xlabel("Weight")
plt.ylabel("Reps")
plt.colorbar(scatter, label="Cluster")

plt.tight_layout()
plt.savefig("kmeans_clustering.png")
plt.close()
