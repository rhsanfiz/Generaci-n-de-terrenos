import random
import png
import time

dimensionX = int(input("Dimensión en X de la matriz: "))
dimensionZ = int(input("Dimensión en Z de la matriz: "))
iteraciones = int(input("Cantidad de iteraciones: "))
matriz = [[0 for z in range(dimensionZ)] for x in range(dimensionX)]
d = 1
dd = d/iteraciones

##  ><
def mini(a,x,y):
    minimo = ""
    for i in range(x):
        for j in range(y):
            if i == 0 and j == 0:
                minimo = int(a[i][j])
            elif int(a[i][j]) < minimo:
                minimo = int(a[i][j])
    return minimo

def maxi(a,x,y):
    maximo = 0
    for i in range(x):
        for j in range(y):
            if i == 0 and j == 0:
                maximo = int(a[i][j])
            elif int(a[i][j]) > maximo:
                maximo = int(a[i][j])
    return maximo

def iteracion(dx,dz,i):
    global matriz, d, dd
    d = d-dd*i
    x1 = random.randint(1,dx)
    y1 = random.randint(1,dz)
##    x1 = round(dx/2)
##    y1 = round(dz/2)
    x2 = x1
    while x1 == x2:
        x2 = random.randint(1,dx)
    y2 = random.randint(1,dz)
    m = (y2-y1)/(x2-x1)*10

    b = y1-x1*m
##    m = random.randint(-120,120)/10
##    b = random.randint(-dz,dz)
##    print(m)
    y = None
    for x in range(dx):
        y = x*m+b
        for z in range(dz):
            if m >= 0:
                if z >= y:
                    matriz[x][z] -= d
                else:
                    matriz[x][z] += d
            else:
                if z <= y:
                    matriz[x][z] += d
                else:
                    matriz[x][z] -= d



horaComienzo = time.time()

for i in range(iteraciones):
    iteracion(dimensionX,dimensionZ,i)
diferencia_a_0 = int(mini(matriz,dimensionX,dimensionZ)) * -1
maximo = maxi(matriz,dimensionX,dimensionZ) + diferencia_a_0
for i in range(dimensionX):
        for j in range(dimensionZ):
            matriz[i][j] = round((int(matriz[i][j]) + diferencia_a_0) * 255 / maximo)
png.from_array(matriz,'L').save(str(random.randint(1,999999))+".png")
print("Proceso finalizado luego de ", str(round(time.time()-horaComienzo)), " segundos")
