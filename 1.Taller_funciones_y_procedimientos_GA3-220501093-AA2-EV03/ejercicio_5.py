# Elaborar un algoritmo que permita ingresar 20 números y muestre todos los números menores e
# iguales a 25.
numeros_arreglo = [] 
numeros_resultado= []
contador = 1

while len(numeros_arreglo) <25:
    try:
        datos_numericos = int (input(f"Ingrese el dato {contador} :"))
        numeros_arreglo.append(datos_numericos)
        contador = contador + 1
        if len(numeros_arreglo) >=25:
            break
    except ValueError:
        print ("Debe ingresar un número valido ")

for dato in numeros_arreglo:
    if dato <= 25:
        numeros_resultado.append(dato)

print(f"los números menores e iguales a 25 son:  {numeros_resultado}")






# while len(numeros_arreglo) <25:
#         datos_numericos = int (input("Ingrese los números: "))
#         numeros_arreglo.append(datos_numericos)
#         if len(numeros_arreglo) >=25:
#             break
  
# for dato in numeros_arreglo:
#     if dato <= 25:
#         print(dato)


#print(numeros_arreglo)