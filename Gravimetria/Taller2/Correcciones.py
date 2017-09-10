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

# VARIABLES

x1 = hoja1[:, 0]
x2 = hoja2[:, 0]
h1 = hoja1[:, 1]
h2 = hoja2[:, 1]
g1 = hoja1[:, 2]
g2 = hoja2[:, 2]

# FUNCION CORRECCION BOURGER

def bourguer(p, h):
    g = - 2 * np.pi * G * p * h
    g = g / 10**(-5)
    return g

# Datos primera hoja

cor_b1 = bourguer(pc1, h1)
cor_b2 = bourguer(pc2, h1)
cor_b3 = bourguer(pc3, h1)
cor_b4 = bourguer(pc4, h1)
cor_b5 = bourguer(pc5, h1)

# Datos segunda hoja

cor_b = bourguer(pc1, h2)

# FUNCION CORRECCION AIRE LIBRE

def aire(h):
    g = 0.308 * h
    return g

# Dato primera hoja

cor_a1 = aire(h1)

# Datos segunda hoja

cor_a2 = aire(h2)

# ANOMALIA BOURGER
# Datos primera hoja

an_b1 = g1 + cor_a1 + cor_b1
an_b2 = g1 + cor_a1 + cor_b2
an_b3 = g1 + cor_a1 + cor_b3
an_b4 = g1 + cor_a1 + cor_b4
an_b5 = g1 + cor_a1 + cor_b5

# Datos segunda hoja

an_b = g2 + cor_a2 + cor_b

# GRAFICA DE TOPOGRAFIA

plt.plot(x1, h1)

plt.title("$TOPOGRAFIA$ $PRIMERA$ $PARTE$ $DEL$ $VOLCAN$")
plt.xlabel("$Distancia(m)$")
plt.ylabel("$Elevacion(m)$")
#plt.show()
plt.close()

# GRAFICA METODO NETTLETON

plt.plot(x1, an_b1, label = "$p_1 = 2655$ $Optima$")
plt.plot(x1, an_b2, label = "$p_2 = 2600$")
plt.plot(x1, an_b3, label = "$p_3 = 2500$")
plt.plot(x1, an_b4, label = "$p_4 = 2700$")
plt.plot(x1, an_b5, label = "$p_5 = 2800$")

plt.legend(loc = 0, title = "$Densidades$ $Propuestas$")
plt.title("$METODO$ $DE$ $NETTLETON$")
plt.xlabel("$Distancia (m)$")
plt.ylabel("$Anomalia$ $Bourger (mGal)$")
#plt.show()
plt.close()

# Half-Width

g_m = np.amax(an_b) / 2
dif = an_b - g_m
half = np.argmin(abs(dif))

half_w = x2[half]
g_med = an_b[half]

# GRAFICA TOPOGRAFIA Y NETTLETON

plt.plot(x2, an_b, label = "$p = 2655$")
plt.scatter(half_w, g_med)

plt.title("$ANOMALIA$ $DE$ $BOURGUER$ $EN$ $VOLCAN$")
plt.xlabel("$Distancia(m)$")
plt.ylabel("$Anomalia$ $Bourger (mGal)$")
plt.legend(loc = 0, title = "$Densidad$ $Optima$")
#plt.show()
plt.close()

# RADIO DE LA ESFERA

z = 1.306 * half_w
p_d = 200.

arriba = 3. * an_b * (x2**2 + z**2)**(3/2)
abajo = 4. * np.pi * G * p_d * z

r = (arriba / abajo)**(1/3)
print r[1]
