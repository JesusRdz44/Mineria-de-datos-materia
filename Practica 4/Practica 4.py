import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("../Practica 1/Entrenamiento_gym.csv")
top5_ejercicios = df["Exercise Name"].value_counts().head(5).index.tolist()
print("Ejercicios comparados:", top5_ejercicios)
grupos = {ex: df[df["Exercise Name"] == ex]["Weight"] for ex in top5_ejercicios}
for ex, datos in grupos.items():
    print(f"  {ex}: n={len(datos)}, media={datos.mean():.1f}, "
          f"mediana={datos.median():.1f}, std={datos.std():.1f}")

# Se prueba si los datos siguen una distribucion normal antes de elegir la prueba a usar. Se usa una muestra de 500 por grupo
print("\nPrueba de normalidad (Shapiro-Wilk) por ejercicio:")
alpha = 0.05
todos_normales = True
for ex, datos in grupos.items():
    muestra = datos.sample(min(500, len(datos)), random_state=1)
    stat, p = stats.shapiro(muestra)
    normal = p > alpha
    todos_normales = todos_normales and normal
    print(f"  {ex}: p={p:.4f} -{'Normal' if normal else 'NO normal'}")


# Si algun grupo no es normal, no se puede usar ANOVA. En ese caso se usa Kruskal-Wallis, que compara los grupos sin necesitar esa forma
if todos_normales:
    print("Todos los grupos son normales - se aplica ANOVA")
    stat, p_valor = stats.f_oneway(*grupos.values())
    prueba_usada = "ANOVA"
else:
    print("Al menos un grupo NO es normal - se aplica Kruskal-Wallis")
    stat, p_valor = stats.kruskal(*grupos.values())
    prueba_usada = "Kruskal-Wallis"
print(f"{prueba_usada}: estadístico={stat:.2f}, p-valor={p_valor:.6f}")
if p_valor < alpha:
    print(f"p-valor < {alpha} - Existe diferencia significativa entre "
          f"al menos un par de ejercicios.")
else:
    print(f"p-valor >= {alpha} - No hay evidencia de diferencia "
          f"significativa entre los ejercicios.")

ex1, ex2 = top5_ejercicios[0], top5_ejercicios[1]
g1, g2 = grupos[ex1], grupos[ex2]
print(f"\nComparación específica: '{ex1}' vs '{ex2}'")
if todos_normales:
    stat2, p2 = stats.ttest_ind(g1, g2, equal_var=False)
    print(f"Prueba t (Welch): t={stat2:.2f}, p-valor={p2:.6f}")
else:
    stat2, p2 = stats.mannwhitneyu(g1, g2, alternative="two-sided")
    print(f"Mann-Whitney U: U={stat2:.0f}, p-valor={p2:.6f}")

if p2 < alpha:
    print(f"p-valor < {alpha} -> '{ex1}' y '{ex2}' tienen pesos "
          f"significativamente distintos.")
else:
    print(f"p-valor >= {alpha} - No hay diferencia significativa entre "
          f"'{ex1}' y '{ex2}'.")

plt.figure(figsize=(9, 5))
plt.boxplot([grupos[ex] for ex in top5_ejercicios],
            tick_labels=top5_ejercicios, patch_artist=True)
plt.title(f"Distribución de peso por ejercicio ({prueba_usada}, "
          f"p={p_valor:.4f})")
plt.ylabel("Weight")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("boxplot_prueba_estadistica.png")
plt.close()
