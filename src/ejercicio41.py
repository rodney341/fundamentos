'''
1- Escriba una lista con el cuadrado de todos los números del 1 al 1200 e imprímala por
pantalla.
'''
lista=[]
aux=1
for x in range(1,1200):
    lista.append(x*x)

for x in range(0,len(lista)):
    print(lista[x])