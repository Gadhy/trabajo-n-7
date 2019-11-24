#imprimir la temperatura ideal

import os
z=int(os.sys.argv[1])
z_invalido=(z<0 or z>37)

while(z_invalido==True):
    z=int(os.sys.argv[1])
    z_invalido=(z<0 or z>37)

for i in range(z):
    print(i)

#fin iterador en rango

print("fin del bucle")

