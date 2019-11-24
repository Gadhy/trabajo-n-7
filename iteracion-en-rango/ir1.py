#imprimir las nota "x"

import os
x=int(os.sys.argv[1])

x_invalido=(x<0 or x>20)

while(x_invalido==True):
    x=int(os.sys.argv[1])
    x_invalido=(x<0 or x>20)

for i in range(x):
    print(i)

#fin iterador en rango

print("fin del bucle")





