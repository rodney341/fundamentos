def C_real(a,b,c):
    y=b*b-4*a*c
    return y

a=int(input("ingrese el coeficiente a: "))
b=int(input("ingrese el coeficiente b: "))
c=int(input("ingrese el coeficiente c: "))

y=C_real(a, b, c)
if y<0:
    print("La ecuación no tiene soluciones reales")
elif a!=0:
    z1=(-b+y**0.5)/(2*a)
    z2=(-b-y**0.5)/(2*a)
    print(z1)
    print(z2)
else:
    print("La ecuación no tiene soluciones reales")