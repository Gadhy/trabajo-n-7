import os

#DECODIFICAR MENSAJE ENCRIPTADO
#input
msg=os.sys.argv[1].upper()

#bucle
for codigo in msg:
    if codigo=="&":
        print("Hola")
    if codigo =="°":
        print("Buenas")
    if codigo=="©":
        print("noches")
    if codigo=="╝":
        print("cuidese")

print("\n")
print("fin del bucle")
