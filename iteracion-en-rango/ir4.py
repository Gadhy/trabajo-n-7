#imprimir las edad hasta "n"

import os
n=int(os.sys.argv[1])

n_invalido=(n<0 or n>10)

while(n_invalido==True):
    n=int(os.sys.argv[1])
    n_invalido=(n<0 or n>10)

for i in range(n):
    print(i)

#fin iterador en rango

print("fin del bucle")





