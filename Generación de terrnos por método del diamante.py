import random
import time
import png


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

def rand(d):
    a = random.randint(-d,d)
    return a
def iteracion(matriz,iteracion,d,r):
    
##    nueva division
    
    base = 1+2**iteracion
    nueva_matriz = [["" for z in range(base)] for x in range(base)]
    for i in range(1+2**(iteracion-1)):
        for j in range(1+2**(iteracion-1)):
            nueva_matriz[2*i][2*j] = matriz[i][j]

            
##    diamantes
    for i in range(round((base-1)/2)):
        for j in range(round((base-1)/2)):
            nueva_matriz[2*i+1][2*j+1] = int(round((nueva_matriz[2*i][2*j]+nueva_matriz[2*i+2][2*j]+nueva_matriz[2*i][2*j+2]+nueva_matriz[2*i+2][2*j+2])/4))+rand(d)


##    cuadrados

    matriz_auxiliar = nueva_matriz
    for i in range(base):
        for j in range(base):
            if nueva_matriz[i][j] == "":
##                print("sssss",i,j)
                
                aux1 = i-1 if matriz_auxiliar[i-1][j] != "" else i-2
                try:
                    aux2 = i+1 if matriz_auxiliar[i+1][j] != "" else 0#i+2
                except IndexError:
                    aux2 = 0
                aux3 = j-1 if matriz_auxiliar[i][j-1] != "" else j-2
                try:
                    aux4 = j+1 if matriz_auxiliar[i][j+1] != "" else 0#j+2
                except IndexError:
                    aux4 = 0

##                print(aux1,j)
##                print(aux2,j)
##                print(i,aux3)
##                print(i,aux4)
                
                nueva_matriz[i][j] = int(round((int(matriz_auxiliar[aux1][j])+int(matriz_auxiliar[aux2][j])+int(matriz_auxiliar[i][aux3])+int(matriz_auxiliar[i][aux4]))/4))+rand(d)

    d = d*(2**-r)

    return nueva_matriz    


iteraciones = int(input("Cantidad de iteraciones: "))
d = int(input("Desvío: "))
r = int(input("Rugosidad: "))
horaComienzo = time.time()
matriz = [[rand(d),rand(d)],[rand(d),rand(d)]]


for i in range(iteraciones):
    matriz = iteracion(matriz,i+1,d,r)


diferencia_a_0 = int(mini(matriz,1+2**iteraciones,1+2**iteraciones)) * -1
maximo = maxi(matriz,1+2**iteraciones,1+2**iteraciones) + diferencia_a_0
for i in range(1+2**iteraciones):
        for j in range(1+2**iteraciones):
            matriz[i][j] = round((int(matriz[i][j]) + diferencia_a_0) * 255 / maximo)
    
png.from_array(matriz,'L').save(str(random.randint(1,999999))+".png")
print("Proceso finalizado luego de ", str(round(time.time()-horaComienzo)), " segundos")


'''Bueno, lo que hay que hacer es que cada paso
duplique la matriz en cada dimensión (la cuadruplica porque va al cuadrado)
agregándole espacios en el medio.

Esto se hace agregando ""s o 0s a la mitad nueva (en ambas dimensiones,
por lo que 3/4 de la matriz van a ser espacios vacíos).
La matriz tiene forma de 2**n +1














'''
