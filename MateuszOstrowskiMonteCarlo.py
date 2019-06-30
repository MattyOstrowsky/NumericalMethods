
"""
Mateusz Ostrowski
216708

Obliczenie wartości składowych tensora momentu kwadrupolowego
jednorodnie naładowanej bryły za pomocą całkowania metodą Monte-Carlo.

"""
import numpy as np
from numpy import random as rnd
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



n = 100000  # liczba punktow
ro =1 # gęstość ładunku

# Wymiary bryly
A = 6
B = 3
C = 3

V = 4/3*np.pi*A*B*C  # objetosc stożka
xmin = -A
xmax = A
ymin = -B
ymax = B
zmin = 0
zmax = C

# Listy punktow

punkty = []
x = []
y = []
z = []



# Maksymalne wartosci funkcji podcalkowej dla wszystkich kombinacji a b
Dmax = [2*xmax**2, 2*ymax**2, 2*zmax**2, 0.75*xmax*ymax, 0.75*xmax*zmax, 0.75*ymax*zmax]
Dmin = [-0.5*(ymax**2 + zmax**2), -0.5*(xmax**2+zmax**2), -0.5*(ymax**2+xmax**2), 0.75*xmin*ymax,
        0.75*xmin*zmax, 0.75*ymin*zmax]



# Losowanie punktow
px = np.array([rnd.uniform(xmin, xmax) for e in range(n)])
py = np.array([rnd.uniform(ymin, ymax) for ee in range(n)])
pz = np.array([rnd.uniform(zmin, zmax) for eee in range(n)])


# Sprawdzanie, ktore punkty naleza do bryly
for i in range(n):
    flaga = False
    if px[i]**2/A**2 + py[i]**2/B**2 + pz[i]**2/C**2 <= 1:
        flaga = True

    if flaga:
        # dopisanie do listy punktow i wylosowanie do kazdego punktu zestawu wartosci funkcji
        punkty.append([px[i], py[i], pz[i], rnd.uniform(Dmin[0], Dmax[0]), rnd.uniform(Dmin[1], Dmax[1]),
                       rnd.uniform(Dmin[2], Dmax[2]), rnd.uniform(Dmin[3], Dmax[3]),
                       rnd.uniform(Dmin[4], Dmax[4]), rnd.uniform(Dmin[5], Dmax[5])])

# Liczba nowych dobrych punktow
N = len(punkty)

# Stworzenie trzech list zawierajacyh dobre punkty potrzebne do wykresow
for ii in range(N):
    x.append(punkty[ii][0])
    y.append(punkty[ii][1])
    z.append(punkty[ii][2])


k = np.array([x,y,z]) # macierz pomocnicza

def f(i, j): # funkcja podcałkowa
    if i == j:
        return (3*k[i]*k[j]-(x**2+y**2+z**2))*ro
    else:
        return (3*k[i]*k[j])*ro

# Plotting
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212, projection='3d')
ax1.plot(x, y, ',b')
ax1.set_title('Podstawa bryly')
ax1.axis('equal')
ax2.scatter(x, y, z, marker=',')
ax2.set_title('Bryla')
ax2.set_xlabel('os X')
ax2.set_ylabel('os Y')
ax2.set_zlabel('os Z')
plt.grid()
plt.show()

x = np.asarray(x)
y = np.asarray(y)
z = np.asarray(z)

D = np.zeros((3,3)) # funkcja podcałkowa

maxD = np.array(D)
minD = np.array(D)

for i in range(3):
    for j in range(3):
        maxD[i][j] = np.max(f(i,j))
        minD[i][j] = np.min(f(i,j))

l = (np.min(minD)-np.max(maxD))*np.random.rand(len(x))+np.max(maxD)

# szacowanie całki metodą Monte-Carlo

for i in range(3):
    for j in range(3):
        D[i][j] = (np.sum((l > 0) & (l< f(i,j)))-sum((l<0) & (l> f(i,j))))/len(x)*V


print("\nWyznaczona macierz momentu kwadrupolowego stożka D ma postać:\n")
print(D)
if np.array_equal(D, np.transpose(D)):
    print("Wynik jest prawidłowy!")
else:
    print("Wynik jest błędny!")

print(np.trace(D))