"""
Created on Tue Oct 29 11:33:29 2024

@author: Mario
"""

import pandas as pd
import matplotlib.pyplot as plt  # Corregido: pyplot en lugar de pylot
#cargar un conjunto de datos en formato CSV
datos = pd.read_csv("covid_impact_on_work new.csv")

#Exploracion basica
print(datos.head(10))
print(datos.tail(10))
print(datos.describe())
print(datos.info())
print(datos.columns())
print(datos["Stress_Level"])
print(datos[datos["Hours_Worked_Per_Day"]])

#converti de str a int
print(datos[datos["Hours_Worked_Per_Day"].astype(str).astype(int)])

#filtrar datos de acuerdo a una condicion
print(datos[datos["Hours_Worked_Per_Day"]>7])
