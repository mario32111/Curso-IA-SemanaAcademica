import statistics as st
import numpy as np
import pandas as pd

def calcular_estadisticos (numeros):
    media = st.mean(numeros)
    mediana = st.median(numeros)
    moda = st.mode(numeros)
    return media, mediana, moda

numeros = [10, 20, 30, 40, 50]
media, mediana, moda = calcular_estadisticos(numeros)

print("Media: ", mediana)
print("Mediana: ", mediana)
print("Moda: ", moda)   