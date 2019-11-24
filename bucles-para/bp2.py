#Sumar los "y" primeros numeros impares
import os

y=int(os.sys.argv[1])
i=1
suma=0

while(i<=y ):
    suma +=i
    i +=2


#fin_del_while

print("la suma de los 5 primeros numeros impares es:", suma)

