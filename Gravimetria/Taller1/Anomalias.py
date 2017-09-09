import numpy as np
import matplotlib.pyplot as plt

# Constantes

G = 6.674 * 10**(-11)
r = 550.
a = 15000
N = 100000
x = np.linspace(-a, a, N)

# Profundidades

z1 = 3000.
z2 = 5000.
z3 = 7000.

# Grosores

h1 = 6000.
h2 = 8000.
h3 = 10000.

# Densidades

ps = 2700.     # Densidad promedio de la corteza continental.
pe1 = 3000.     # Densidad para taller.
pe2 = 2160.     # Densidad promedio de la sal, diapiro.
pe3 = 2800.     # Densidad punto losa.

# FUNCIONES
# Funcion modelaje gravedad esfera

def gravedad_e(x, z, p):
    ge = (4 / 3) * np.pi * G * (r**3) * (p - ps) * (z / (x**2 + z**2)**(3 / 2))
    return ge

# Funcion modejale gravedad cilindro

def gravedad_c(x, z, p):
    gc = 2 * np.pi * G * (r**2) * (p - ps) * (z / (x**2 + z**2))
    return gc

# Funcion modelaje gravedad losa

def gravedad_l(x, z, p, h):
    gl = 2. * G * (p - ps) * h * ((np.pi / 2.) + np.arctan(x / z))
    return gl

# Funciones Half-width

def half_wp(prof, gmed):     # Densidad esfera mayor a terreno.
    j = 0
    for i in range(-N, 0):
	if (prof[i] <= gmed):
	    j = i
	else:
	    break
    return x[j]

def half_wn(prof, gmed):     # Densidad esfera menor a terreno.
    j = 0
    for i in range(-N, 0):
	if (prof[i] >= gmed):
	    j = i
	else:
	    break
    return x[j]

# COMPONENTES
# Componenetes esfera

prof_e1 = gravedad_e(x, z1, pe1)
prof_e2 = gravedad_e(x, z2, pe1)
prof_e3 = gravedad_e(x, z3, pe2)

# Componentes cilindro

prof_c1 = gravedad_c(x, z1, pe1)
prof_c2 = gravedad_c(x, z2, pe1)
prof_c3 = gravedad_c(x, z3, pe2)

# Componentes losa (Grosor h)

prof_l11 = gravedad_l(x, z1, pe1, h1)
prof_l12 = gravedad_l(x, z1, pe1, h2)
prof_l13 = gravedad_l(x, z1, pe1, h3)

# Componentes losa (Densidad pe)

prof_l21 = gravedad_l(x, z1, pe1, h2)
prof_l22 = gravedad_l(x, z1, pe2, h2)
prof_l23 = gravedad_l(x, z1, pe3, h2)

# Componentes losa (Profundidad z)

prof_l31 = gravedad_l(x, z1, pe1, h2)
prof_l32 = gravedad_l(x, z2, pe1, h2)
prof_l33 = gravedad_l(x, z3, pe1, h2)

# GRAVEDAD MEDIA
# Esfera

g_me1 = np.amax(prof_e1) / 2
g_me2 = np.amax(prof_e2) / 2
g_me3 = np.amin(prof_e3) / 2

# Cilindro

g_mc1 = np.amax(prof_c1) / 2
g_mc2 = np.amax(prof_c2) / 2
g_mc3 = np.amin(prof_c3) / 2

# HALF-WIDTH
# Esfera

half_e1 = half_wp(prof_e1, g_me1)
half_e2 = half_wp(prof_e2, g_me2)
half_e3 = half_wn(prof_e3, g_me3)

# Cilindro

half_c1 = half_wp(prof_c1, g_mc1)
half_c2 = half_wp(prof_c2, g_mc2)
half_c3 = half_wn(prof_c3, g_mc3)

# COEFICIENTES
# Esfera

c_e1 = z1 / half_e1
c_e2 = z2 / half_e2
c_e3 = z3 / half_e3

#print c_e1, c_e2, c_e3

# Cilindro

c_c1 = z1 / half_c1
c_c2 = z2 / half_c2
c_c3 = z3 / half_c3

#print c_c1, c_c2, c_c3

# GRAFICAS
# Esfera

plt.plot(x, prof_e1, label = "$p_e > p_s$ $z = 1km$")
plt.plot(x, prof_e2, label = "$p_e > p_s$ $z = 5km$")
plt.plot(x, prof_e3, label = "$p_e < p_s$ $z = 7km$")

plt.scatter(half_e1, g_me1, color = "red")
plt.scatter(half_e2, g_me2, color = "black")
plt.scatter(half_e3, g_me3, color = "blue")

plt.title("$ANOMALIA$ $PARA$ $UNA $ESFERA$")
plt.legend()
plt.xlim(-a, a)
plt.xlabel("$x(m)$")
plt.ylabel("$g(mGal)$")
#plt.show()
plt.close()

# Cilindro

plt.plot(x, prof_c1, label = "$p_e > p_s$ $z = 1km$")
plt.plot(x, prof_c2, label = "$p_e > p_s$ $z = 5km$")
plt.plot(x, prof_c3, label = "$p_e < p_s$ $z = 7km$")

plt.scatter(half_c1, g_mc1, color = "red")
plt.scatter(half_c2, g_mc2, color = "black")
plt.scatter(half_c3, g_mc3, color = "blue")

plt.title("$ANOMALIA$ $PARA$ $UN$ $CILINDRO$")
plt.legend()
plt.xlim(-a, a)
plt.xlabel("$x(m)$")
plt.ylabel("$g(mGal)$")
#plt.show()
plt.close()

# Losa (Grosor h)

plt.plot(x, prof_l11, label = "$h = 6km$")
plt.plot(x, prof_l12, label = "$h = 8km$")
plt.plot(x, prof_l13, label = "$h = 10km$")

plt.title("$ANOMALIA$ $PARA$ $UNA$ $LOSA$ $(Grosor)$")
plt.legend(loc = 0, title = "$p_e = 3000kg/m^3$ \n$z_0 = 3km$")
plt.xlim(-a, a)
plt.xlabel("$x(m)$")
plt.ylabel("$g(mGal)$")
#plt.show()
plt.close()

prof1_l11 = np.diff(prof_l11)
prof1_l12 = np.diff(prof_l12)     # Primera derivada
prof1_l13 = np.diff(prof_l13)

plt.plot(x[1 : N], prof1_l11, label = "$h = 6km$")
plt.plot(x[1 : N], prof1_l12, label = "$h = 8km$")
plt.plot(x[1 : N], prof1_l13, label = "$h = 10km$")

plt.title("$ANOMALIA$ $LOSA$ $dx$ $(Grosor)$")
plt.legend(loc = 0, title = "$p_e = 3000kg/m^3$ \n$z_0 = 3km$")
plt.xlim(-a, a)
plt.xlabel("$x(m)$")
plt.ylabel("$g(mGal)$")
#plt.show()
plt.close()

prof2_l11 = np.diff(prof1_l11)
prof2_l12 = np.diff(prof1_l12)     # Segunda Derivada
prof2_l13 = np.diff(prof1_l13)

plt.plot(x[1 : N - 1], prof2_l11, label = "$h = 6km$")
plt.plot(x[1 : N - 1], prof2_l12, label = "$h = 8km$")
plt.plot(x[1 : N - 1], prof2_l13, label = "$h = 10km$")

plt.title("$ANOMALIA$ $LOSA$ $dx^2$ $(Grosor)$")
plt.legend(loc = 0, title = "$p_e = 3000kg/m^3$ \n$z_0 = 3km$")
plt.xlim(-a, a)
plt.xlabel("$x(m)$")
plt.ylabel("$g(mGal)$")
#plt.show()
plt.close()

# Losa (Densidad pe)

plt.plot(x, prof_l21, label = "$p_p = 3000kg/m^3$")
plt.plot(x, prof_l22, label = "$p_p = 2160kg/m^3$")
plt.plot(x, prof_l23, label = "$p_p = 2800kg/m^3$")

plt.title("$ANOMALIA$ $PARA$ $UNA$ $LOSA$ $(Densidad)$")
plt.legend(loc = 0, title = "$h = 8km$ \n$z_0 = 3km$")
plt.xlim(-a, a)
plt.xlabel("$x(m)$")
plt.ylabel("$g(mGal)$")
#plt.show()
plt.close()

prof1_l21 = np.diff(prof_l21)
prof1_l22 = np.diff(prof_l22)     # Primera Derivada
prof1_l23 = np.diff(prof_l23)

plt.plot(x[1 : N], prof1_l21, label = "$p_p = 3000kg/m^3$")
plt.plot(x[1 : N], prof1_l22, label = "$p_p = 2160kg/m^3$")
plt.plot(x[1 : N], prof1_l23, label = "$p_p = 2800kg/m^3$")

plt.title("$ANOMALIA$ $LOSA$ $dx$ $(Densidad)$")
plt.legend(loc = 0, title = "$h = 8km$ \n$z_0 = 3km$")
plt.xlim(-a, a)
plt.xlabel("$x(m)$")
plt.ylabel("$g(mGal)$")
#plt.show()
plt.close()

prof2_l21 = np.diff(prof1_l21)
prof2_l22 = np.diff(prof1_l22)     # Segunda Derivada
prof2_l23 = np.diff(prof1_l23)

plt.plot(x[1 : N - 1], prof2_l21, label = "$p_p = 3000kg/m^3$")
plt.plot(x[1 : N - 1], prof2_l22, label = "$p_p = 2160kg/m^3$")
plt.plot(x[1 : N - 1], prof2_l23, label = "$p_p = 2800kg/m^3$")

plt.title("$ANOMALIA$ $LOSA$ $dx^2$ $(Densidad)$")
plt.legend(loc = 0, title = "$h = 8km$ \n$z_0 = 3km$")
plt.xlim(-a, a)
plt.xlabel("$x(m)$")
plt.ylabel("$g(mGal)$")
#plt.show()
plt.close()

# Losa (Profundidad z)

plt.plot(x, prof_l31, label = "$z_0 = 3km$")
plt.plot(x, prof_l32, label = "$z_0 = 5km$")
plt.plot(x, prof_l33, label = "$z_0 = 7km$")

plt.title("$ANOMALIA$ $PARA$ $UNA$ $LOSA$ $(Profundidad)$")
plt.legend(loc = 0, title = "$h = 8km$ \n$p_e = 3000kg/m^3$")
plt.xlim(-a, a)
plt.xlabel("$x(m)$")
plt.ylabel("$g(mGal)$")
#plt.show()
plt.close()

prof1_l31 = np.diff(prof_l31)
prof1_l32 = np.diff(prof_l32)     # Primera Derivada
prof1_l33 = np.diff(prof_l33)

plt.plot(x[1 : N], prof1_l31, label = "$z_0 = 3km$")
plt.plot(x[1 : N], prof1_l32, label = "$z_0 = 5km$")
plt.plot(x[1 : N], prof1_l33, label = "$z_0 = 7km$")

plt.title("$ANOMALIA$ $LOSA$ $dx$ $(Profundidad)$")
plt.legend(loc = 0, title = "$h = 8km$ \n$p_e = 3000kg/m^3$")
plt.xlim(-a, a)
plt.xlabel("$x(m)$")
plt.ylabel("$g(mGal)$")
#plt.show()
plt.close()

prof2_l31 = np.diff(prof1_l31)
prof2_l32 = np.diff(prof1_l32)     # Segunda Derivada
prof2_l33 = np.diff(prof1_l33)

plt.plot(x[1 : N - 1], prof2_l31, label = "$z_0 = 3km$")
plt.plot(x[1 : N - 1], prof2_l32, label = "$z_0 = 5km$")
plt.plot(x[1 : N - 1], prof2_l33, label = "$z_0 = 7km$")

plt.title("$ANOMALIA$ $LOSA$ $dx^2$ $(Profundidad)$")
plt.legend(loc = 0, title = "$h = 8km$ \n$p_e = 3000kg/m^3$")
plt.xlim(-a, a)
plt.xlabel("$x(m)$")
plt.ylabel("$g(mGal)$")
#plt.show()
plt.close()
