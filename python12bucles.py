print("Ejemplo bucles 1")
print("WHILE")
# NECESITAMOS UNA VARIABLE PARA LA CONDICION DEL BUCLE
contador = 0
while (contador <= 5):
    # DEBEMOS INDICAR QUE SALDREMOS DEL BUCLE
    print("Contador ", contador)
    contador = contador + 1
# basicamente el contador +1 porque si no seria siempre 0 y eso seria un bucle infinito, al ponerle contador + 1, el contador se va
#incrementando y como la condicion es <=5, en el momento que llega a 5 se para.    
print("Fin de programa")
print("Ejemplo bucles2")
print("For")
# NORMALMENTE LAS VARIABLES DE LOS BUCLES CONTADORES
# SE REPRESENTAN CON UNA SOLA LETRA (i, z, j)
# la i viene de index, las z y j se utilizan para estructuras mas complejas
for i in range(5):
    print("Valor de i ", i)
for i in range(1 , 6):
    print("Valor i: ", i)

print("WHILE")
# NECESITAMOS UNA VARIABLE PARA LA CONDICION DEL BUCLE
contador = 0
while (contador <= 5):
    # DEBEMOS INDICAR QUE SALDREMOS DEL BUCLE
    print("Contador ", contador)
    contador = contador + 1

print("Fin de programa")
