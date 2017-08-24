import numpy as np
import matplotlib.pyplot as plt

# LECTURA DE DATOS

hoja1 = np.genfromtxt('hoja1.txt')
hoja2 = np.genfromtxt('hoja2.txt')

# CONSTANTES Y DENSIDADES

G = 6.674 * 10**(-11)
pc1 = 2655
pc2 = 2600
pc3 = 2500
pc4 = 2700
pc5 = 2800

# FUNCION CORRECCION BOURGER

def bourguer(p, h):
    g = - 2 * np.pi * G * p * h
    g = g / 10**(-5)
    return g

# Datos primera hoja

cor_b1 = bourguer(pc1, hoja1[:, 1])
cor_b2 = bourguer(pc2, hoja1[:, 1])
cor_b3 = bourguer(pc3, hoja1[:, 1])
cor_b4 = bourguer(pc4, hoja1[:, 1])
cor_b5 = bourguer(pc5, hoja1[:, 1])

# Datos segunda hoja

cor_b = bourguer(pc1, hoja2[:, 1])

# FUNCION CORRECCION AIRE LIBRE

def aire(h):
    g = 0.308 * h
    return g

# Dato primera hoja

cor_a1 = aire(hoja1[:, 1])

# Datos segunda hoja

cor_a2 = aire(hoja2[:, 1])

# ANOMALIA BOURGER

# Datos primera hoja

an_b1 = hoja1[:, 2] + cor_a1 + cor_b1
an_b2 = hoja1[:, 2] + cor_a1 + cor_b2
an_b3 = hoja1[:, 2] + cor_a1 + cor_b3
an_b4 = hoja1[:, 2] + cor_a1 + cor_b4
an_b5 = hoja1[:, 2] + cor_a1 + cor_b5

# Datos segunda hoja

an_b = hoja2[:, 2] + cor_a2 + cor_b

# GRAFICA DE TOPOGRAFIA

plt.plot(hoja1[:, 0], hoja1[:, 1])
plt.title("Topografia primera parte del volcan")
plt.xlabel("$Distancia (m)$")
plt.ylabel("$Elevacion (m)$")
plt.close()

# GRAFICA METODO NETTLETON

plt.plot(hoja1[:, 0], an_b1, label = "$p_1 = 2655$")
plt.plot(hoja1[:, 0], an_b2, label = "$p_2 = 2600$")
plt.plot(hoja1[:, 0], an_b3, label = "$p_3 = 2500$")
plt.plot(hoja1[:, 0], an_b4, label = "$p_4 = 2700$")
plt.plot(hoja1[:, 0], an_b5, label = "$p_5 = 2800$")
plt.legend()
plt.title("Metodo de Nettleton")
plt.xlabel("$Distancia (m)$")
plt.ylabel("$Anomalia Bourger (mGal)$")
plt.close()

# GRAFICA TOPOGRAFIA Y NETTLETON

plt.plot(hoja2[:, 0], an_b, label = "$p = 2655$")
plt.title("Nettleton")
plt.xlabel("$Distancia (m)$")
plt.ylabel("$Anomalia de Bourger (mGal)$")
plt.legend()
plt.show()
