
import pandas as pd
import matplotlib.pyplot as plt  # Corregido: pyplot en lugar de pylot
#cargar un conjunto de datos en formato CSV
datos = pd.read_csv("football_mini.csv")

ax = plt.subplot()
ax.plot(datos["Value"],datos["Wage"], marker= "o", ms=4, linestyle="")

ax.set_xlabel("Salario")
ax.set_xlabel("Valor")
plt.title("Grafico de dispersion Salario/Valor")
plt.show()