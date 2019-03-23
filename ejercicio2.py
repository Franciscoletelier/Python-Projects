#Realizar un programa que pida un numero
# Si el numero es mayor a cero, mostrar un mensaje que diga POSITIVO
#Si el numero es menor a cero, mostrar un mensaje NEGATIVO
#Si es igua a cero, que diga que es CERO
cifra = input("Ingresa el numero: ")
if cifra < 0:
    print("Negativo")
elif cifra > 0:
    print("Positivo")
else:  
    print ("CERO")
