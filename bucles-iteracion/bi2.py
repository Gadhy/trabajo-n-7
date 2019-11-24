import os

#DECODIFICAR MENSAJE ENCRIPTADO
#input
msg=os.sys.argv[1].upper()

#bucle
for numero in msg:
    if numero=="1":
        print("Juan")
    if numero=="2":
        print("come")
    if numero=="3":
        print("tallarines")
    if numero=="4":
        print("verdes")

print("\n")
print("fin del bucle")
