#Calcular el valor total que una persona debe pagar
# por la compra de un neumatico si tienen la siguiente
# promocion
#Si la cantidad de neumaticos comprados es mayor a 6
#el precio unitario tine un descuento del 15%, 
#Si es menor senalado se dara un descuento del 10%

n = int(input("Neumaticos comprados: "))
p = float(input("Precio Unit:  "))
if n > 6:
    s = n*p 
    d = s*0.15
    total= int(s-d)
else:
    s = n*p
    d = s*0.1
    total = s-d
print "El total a pagar es:  ", total

