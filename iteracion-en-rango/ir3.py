#Imprimir los numeros hasta "y"
import os

y=int(os.sys.argv[1])
y_invalido=(y<0 or y>12)

while(y_invalido==True):
    y=int(os.sys.argv[1])
    y_invalido=(y<0 or y>12)

for i in range(y):
    print(i)

#fin iterador en rango

print("fin del bucle")

