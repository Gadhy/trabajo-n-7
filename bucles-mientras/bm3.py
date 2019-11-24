import os
temperatuta=int(os.sys.argv[1])
print(temperatuta)

temperatuta_invalida=(temperatuta<48 or temperatuta>50)

#validar que la temperatura este entre 48 y 50
while(temperatuta_invalida==True):
    temperatuta=int(os.sys.argv[1])
    temperatuta_invalida=(temperatuta<48 or temperatuta>50)

#fin del while

print("fin el bucle")
