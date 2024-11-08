
import pandas as pd
import matplotlib.pyplot as plt  # Corregido: pyplot en lugar de pylot
#cargar un conjunto de datos en formato CSV
datos = pd.read_csv("football_mini.csv")

ax= plt.subplot()


plt.plot()
plt.title("Relacion Posicion/Salario de Jugadores de Futbol")
ax.set_xlabel("Posicion")
ax.set_ylabel("Salario")
posicion = datos["Position"]
salario = datos ["Wage"]
plt.bar(posicion, salario)
plt.show()

datos_importantes = datos[["Name", "Age", "Nacionality"]]
print(datos_importantes)