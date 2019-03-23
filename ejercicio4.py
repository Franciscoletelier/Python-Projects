#Simular el lanzamiento de un dado, y finaliza
#cuando sean 6 intentos
from random import *
x = 0
while x != 3:
    x = randint (1, 6)
    print(x)

#Como hacer un contador de intentos
from random import *
x = 0
c = 0
while x != 3:
    x = randint (1, 100)
    print(x)
    c = c+1
print "Contador de intentos", c
print(x)

#Como hacer un contador de intentos
#hasta que salga 5
from random import *
x = 0
c = 0
while x == 5:
    x = randint (1, 100)
    print(x)
    c = c+1
print "Contador de intentos", c
print(x)