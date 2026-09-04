import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv("../Practica 1/Entrenamiento_gym.csv")
palabras_pierna = ["squat", "deadlift", "leg", "hack", "glute", "good morning"]
def clasificar_grupo(nombre_ejercicio):
    nombre = nombre_ejercicio.lower()
    for palabra in palabras_pierna:
        if palabra in nombre:
            return "Pierna"
    return "Tren superior"
df["Grupo"] = df["Exercise Name"].apply(clasificar_grupo)
print("Distribución de la variable objetivo:")
print(df["Grupo"].value_counts())
print(f"(Proporción Pierna: {(df['Grupo']=='Pierna').mean()*100:.1f}%)")


X = df[["Weight", "Reps"]]
y = df["Grupo"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# KNN se basa en distancias, asi que las variables deben estar en la misma escala
scaler = StandardScaler()
X_train_esc = scaler.fit_transform(X_train)
X_test_esc = scaler.transform(X_test)
print("\nBúsqueda de mejor k:")
valores_k = [3, 5, 7, 9, 11, 15, 21]
resultados_k = {}
for k in valores_k:
    modelo_k = KNeighborsClassifier(n_neighbors=k)
    modelo_k.fit(X_train_esc, y_train)
    pred_k = modelo_k.predict(X_test_esc)
    acc_k = accuracy_score(y_test, pred_k)
    resultados_k[k] = acc_k
    print(f"  k={k}: accuracy={acc_k:.4f}")
mejor_k = 9
print(f"\nSe elige k={mejor_k}")

# Modelo final y evaluación
modelo = KNeighborsClassifier(n_neighbors=mejor_k)
modelo.fit(X_train_esc, y_train)
predicciones = modelo.predict(X_test_esc)
acc = accuracy_score(y_test, predicciones)
print(f"Modelo final: KNN (k={mejor_k})")
print(f"Precisión (accuracy) en datos de prueba: {acc:.4f}")
print("\nReporte de clasificación:")
print(classification_report(y_test, predicciones))
matriz = confusion_matrix(y_test, predicciones, labels=["Pierna", "Tren superior"])
print("Matriz de confusión:")
print(matriz)

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
# Accuracy vs k
axes[0].plot(list(resultados_k.keys()), list(resultados_k.values()),
             marker="o")
axes[0].axvline(mejor_k, color="red", linestyle="--",
                 label=f"k elegido = {mejor_k}")
axes[0].set_title("Precisión del modelo según el valor de k")
axes[0].set_xlabel("k (número de vecinos)")
axes[0].set_ylabel("Accuracy")
axes[0].legend()
# Matriz de confusión
im = axes[1].imshow(matriz, cmap="Blues")
axes[1].set_xticks([0, 1])
axes[1].set_yticks([0, 1])
axes[1].set_xticklabels(["Pierna", "Tren superior"])
axes[1].set_yticklabels(["Pierna", "Tren superior"])
axes[1].set_xlabel("Predicho")
axes[1].set_ylabel("Real")
axes[1].set_title("Matriz de confusión")
for i in range(2):
    for j in range(2):
        axes[1].text(j, i, matriz[i, j], ha="center", va="center",
                      color="black", fontsize=12)
plt.tight_layout()
plt.savefig("knn_clasificacion.png")
plt.close()
