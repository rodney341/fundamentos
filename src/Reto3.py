numero = input("numero: ")
aux=0
for x in numero:
    aux=aux+1
if aux ==2:
    print("unidad")
elif(aux==3):
    print("decena")
elif(aux==4):
    print("centena")
elif(aux==5):
    print("milesima")
elif(aux==6):
    print("decena de mil")
elif(aux==7):
    print("centena de mil")