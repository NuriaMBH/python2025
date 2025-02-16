print("Ejemplo de librerías")
#SINTAXIS CON from
#from math import floor, ceil, trunc
import math
numero1 = 20
numero2 = 3
division = numero1 / numero2
print("La división es ", division)
# DECLARAMOS VARIABLES PARA ALMACENAR LOS VALORES 

# Almacenamos los valores de las operaciones
varFloor = math.floor(division)
varCeil = math.ceil(division)
varTrunc = math.trunc(division)
print("Floor ", varFloor)
print("Ceil ", varCeil)
print("Trunc ", varTrunc)
print("Fin de programa")

# 1. floor(x) → Redondeo hacia abajo
# La función floor(x) devuelve el entero más cercano por debajo del número dado.

from math import floor

print(floor(4.9))  # Devuelve 4
print(floor(-3.7)) # Devuelve -4 (porque es el entero menor más cercano por debajo del número dado.

#2. ceil(x) → Redondeo hacia arriba
#La función ceil(x) devuelve el entero más cercano por encima del número dado.
from math import ceil

print(ceil(4.1))   # Devuelve 5
print(ceil(-3.7))  # Devuelve -3 (el entero mayor más cercano)

#3. trunc(x) → Elimina la parte decimal (truncamiento)
#La función trunc(x) simplemente elimina la parte decimal, sin importar si el número es positivo o negativo.

from math import trunc

print(trunc(4.9))   # Devuelve 4
print(trunc(-3.7))  # Devuelve -3

#Diferencia con floor() y ceil()

# trunc(x) simplemente corta la parte decimal sin redondear.
# floor(x) y ceil(x) sí redondean dependiendo de si el valor es positivo o negativo.
