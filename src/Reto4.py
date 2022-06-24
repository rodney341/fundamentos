Tupla = (1, 2, "Hola", 3.3, "hello", 5, 4.3)
enteros=[]
reales=[]
caracteres=[]
for x in Tupla:
    if type(x)==int:
        enteros.append(x)
    if type(x)==float:
        reales.append(x)
    if type(x)==str:
        caracteres.append(x)
        
print("Datos de tipo int")        
print(enteros)
print("Datos de tipo float")
print(reales)
print("Datos de tipo str")
print(caracteres)        