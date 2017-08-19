import numpy as np
import matplotlib.pyplot as plt

# Constantes

G = 6.674 * 10**(-11)
r = 500.

a = 15000
N = 200000
x = np.linspace(-a, a, N)

# Profundidades

z1 = 3000.
z2 = 5000.
z3 = 7000.

# Densidades

ps = 2700.     # Densidad promedio de la corteza continental

pe1 = 3000.
pe2 = 2160.     # Densidad promedio de la sal, diapiro

# Funcion modelaje gravedad

def gravedad(x, z, p):
    y = (4 / 3) * np.pi * G * (r**3) * (p - ps) * (z / (x**2 + z**2)**(3 / 2))
    return y

# Componenetes

prof1 = gravedad(x, z1, pe1)
plt.plot(x, prof1, label = "$p_e > p_s, 1km$")

prof2 = gravedad(x, z2, pe1)
plt.plot(x, prof2, label = "$p_e > p_s, 5km$")

prof3 = gravedad(x, z3, pe2)
plt.plot(x, prof3, label = "$p_e < p_s, 7km$")

# Grafica

plt.title("Anomalias a diferentes profundidades y densidades")
plt.legend()
plt.xlabel("$x$")
plt.ylabel("$g$")
#plt.show()
plt.close()

# Half-with

def half_with(prof):
    maxi = prof.argmax()
    g = prof[maxi] / 2
    half = np.where(prof == g)[0]
    return half

half1 = half_with(prof1)

print half1

max_1 = prof1.argmax()
g1 = prof1[max_1] / 2
h1 = np.where(prof1 == g1)[0]

print h1
