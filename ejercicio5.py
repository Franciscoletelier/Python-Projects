#En un cultivo se tiene una catidad de bacterias iniciales
#cada dia esta cantidad de bacterias
#esta cantidad se duplica
#Determine en que dia la cantidad de bacterias
#excede a un valor maximo

from random import *
inicial = int(input("Cantidad inicial: "))
max=int(input("Cantidad max: "))
dia = 0
while inicial <=max:
    inicial = inicial*2
    print "Inicial", inicial
    dia = dia + 1
    print "Dia", dia
print "Cantidad bacterias excede al max: ", dia
