import os
años=int(os.sys.argv[1])
print(años)

años_invalidos=(años<2000 or años>2010)

#validar que los años ente entre 2000 y 2010
while(años_invalidos==True):
    años=int(os.sys.argv[1])
    años_invalidos=(años<2000 or años>2010)

#fin del while

print("fin del bucle")
