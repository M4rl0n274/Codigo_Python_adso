# Escriba un programa que lea dos vectores de números enteros ordenados ascendentemente y
# luego produzca la lista ordenada de la mezcla de los dos, por ejemplo, si los dos arreglos tienen los
# números 1 3 6 9 17 y 2 4 10 17, respectivamente, la lista de números en la pantalla debe ser 1 2 3 4
# 6 9 10 17 17. Limite los vectores a un tamaño de 5 y debe validar en cada ingreso que realmente se
# estén ingresando los datos de forma ascendente.


def leer_vector(nombre_vector, limite=5):

    vector = []
    print(f"\nLeyendo {nombre_vector}:")
    
    # Primer dato (sin comparación)
    while True:
        try:
            dato = int(input("Ingrese el dato #1: "))
            if dato < 0:
                print("Error: No ingrese números negativos.")
                continue
            vector.append(dato)
            break
        except ValueError:
            print("Error: Ingrese un número entero válido.")

    # Siguientes datos
    while len(vector) < limite:
        try:
            dato = int(input(f"Ingrese el dato #{len(vector)+1}: "))
            
            if dato < 0:
                print("Error: No ingrese números negativos.")
                continue

            if dato <= vector[-1]:
                print(f"Error: el dato ({dato}) no es mayor que el anterior ({vector[-1]}).")
                continue

            vector.append(dato)

        except ValueError:
            print("Error: Ingrese un número entero válido.")

    return vector

primer_vector = leer_vector("primer vector")
segundo_vector = leer_vector("segundo vector")

mezcla = sorted(primer_vector + segundo_vector)

print("\nPrimer vector:", primer_vector)
print("Segundo vector:", segundo_vector)
print("Vector mezclado ordenado:", mezcla)




































# primer_vector = []
# segundo_vector = []
# limite_vector = 0
# contador = 1

# print ("\nLeyendo primer vector")
# dato_anterior = int (input(f"Ingrese el dato #{contador}: "))
# primer_vector.append(dato_anterior)

# def datos_vectores ():
#     while True:
#         contador +=1
#         dato_nuevo = int (input(f"Ingrese el dato #{contador}: "))

#         if dato_nuevo < 0 or dato_anterior < 0:
#             print("Error: No ingrese numeros menores a 0")
#             continue
        
#         if dato_nuevo <= dato_anterior:
#             print(f"EL dato ingresado ({dato_nuevo}) no es mayor que el anterior o es igual")
#         else:
#             dato_anterior = dato_nuevo
#             primer_vector.append(dato_nuevo)
#             limite_vector += 1 
        
#         if limite_vector == 4:
#             break

#     return primer_vector



# print(f"Impresión de prueba primer vector{primer_vector}")