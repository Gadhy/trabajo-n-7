import os
hora=int(os.sys.argv[1])
print(hora)

hora_inadecuada=(hora>12 or hora<10)

#validar que la hora este entre las 10 y 12

while(hora_inadecuada==True):
    hora=int(os.sys.argv[1])
    hora_inadecuada=(hora>12 or hora<10)

#fin del while

print("fin del bucle")
