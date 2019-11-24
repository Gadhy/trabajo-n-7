import os
edad=int(os.sys.argv[1])
print(edad)

edad_invalida=(edad<6 or edad>10)

#validar que la edad este entre 6 y 10 para asistir a una fiesta infantil

while(edad_invalida==True):
    edad=int(os.sys.argv[1])
    edad_invalida=(edad<6 or edad>10)

#fin del bucle

print("fin del bucle")
