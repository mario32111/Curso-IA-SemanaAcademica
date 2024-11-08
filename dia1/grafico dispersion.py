
import pandas as pd
import matplotlib.pyplot as plt  # Corregido: pyplot en lugar de pylot
#cargar un conjunto de datos en formato CSV
datos = pd.read_csv("football_mini.csv")

ax = plt.subplot()
ax.scatter(x = datos["Value"], y = datos["Wage"])
ax.set_xlabel("Salario")
ax.set_xlabel("Valor")
plt.title("Grafico de dispersion Salario/Valor")
plt.show()