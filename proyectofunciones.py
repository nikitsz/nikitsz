import os
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import math
import numpy as np

def buscar_archivos():
    archivos = []

    for archivo in os.listdir():
        if archivo.endswith(".npy"):
            archivos.append(archivo)
    return archivos        

def imprimir_opciones(lista_archivos):
    for i in range(len(lista_archivos)):
        numero = i+1
        print(f"{numero}. {lista_archivos[i]}")
    while True:
        elegir = int(input("elija el archivo a trabajar: "))
        if elegir < 1 or elegir > len(lista_archivos):
            print("Error, vuelva a ingresar un numero")
            continue
        else:
            break
    return lista_archivos[elegir-1]  

def cargar_senal(nombre_archivo):
    senal = np.load(nombre_archivo)
    return senal.tolist()
#calcular mediana
def calcular_mediana(datos_senal):
    resultados = []
    for i in range(len(datos_senal)):
        ventana = datos_senal[i:i+7]
        resultados.append(np.median(ventana))
    return resultados
#calcular media
def calcular_media(datos_senal):
    resultados = []
    for i in range(len(datos_senal)):
        ventana = datos_senal[i:i+7]
        resultados.append(np.mean(ventana))
    return resultados
archivos_encontrados = buscar_archivos()
archivo_elegido = imprimir_opciones(archivos_encontrados)
datos_senal = cargar_senal(archivo_elegido)
datos_mediana = calcular_mediana(datos_senal)
datos_media = calcular_media(datos_senal)
