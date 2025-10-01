limite_datos = 5
contador = 1
vector = []
print("leyendo vector 0")
dato_anterior = int(input("Ingrese el dato: "))
vector.append(dato_anterior)

while contador < limite_datos:
    dato_nuevo = int(input("Ingrese el dato: "))
    if dato_nuevo <= dato_anterior:
        print ("El dato ingresado no es mayor que el anterior.")        
    else:
        dato_anterior = dato_nuevo
        vector.append(dato_nuevo)
        contador = contador + 1

print (vector)


print("leyendo vector 1")
vector1 = []
contador = 1
dato_anterior = int(input("Ingrese el dato: "))
vector1.append(dato_anterior)

while contador < limite_datos:
    dato_nuevo = int(input("Ingrese el dato: "))
    if dato_nuevo <= dato_anterior:
        print ("El dato ingresado no es mayor que el anterior.")        
    else:
        dato_anterior = dato_nuevo
        vector1.append(dato_nuevo)
        contador = contador + 1

print (vector)
print (vector1)

