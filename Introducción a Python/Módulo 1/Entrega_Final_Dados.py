# Tendrás que crear un programa que simule la tirada de dados.
# Cada vez que ejecutamos el programa, este elegirá dos números
# aleatorios entre el 1 y el 6. El programa deberá imprimirlos en pantalla,
# imprimir su suma y preguntarle al usuario si quiere tirar los dados otra vez.

import random

n=1

while n==1:
    print("A continuación se tiran dos dados y se muestra su suma:")
    x=random.choice([1,2,3,4,5,6])
    y=random.choice([1,2,3,4,5,6])
    z=x+y
    print("Dado 1: ",x)
    print("Dado 2: ",y)
    print("La suma de ambos dados es: ",z)
    n=int(input("Si desea volver a tirar los dados ingrese 1, si desea finalizar ingrese 0: "))