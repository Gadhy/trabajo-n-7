import os
minutos=int(os.sys.argv[1])
print(minutos)

minutos_invalidos=(minutos<6 or minutos>8)

#validar la temperatura que este entre 6 y 8

while(minutos_invalidos==True):
    minutos=int(os.sys.argv[1])
    minutos_invalidos=(minutos<6 or minutos>8)
#fin del while

print("fin del bucle")
