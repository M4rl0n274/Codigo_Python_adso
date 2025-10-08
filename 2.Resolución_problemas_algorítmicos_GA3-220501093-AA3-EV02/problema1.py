# Desarrollar un programa que permita almacenar las edades de un grupo de 10 personas en un
# vector de enteros y luego determine la cantidad de personas que son menores de edad, mayores
# de edad, cuántos adultos mayores, la edad más baja, la edad más alta y el promedio de edades
# ingresadas. Para el ejercicio anterior, suponga que un adulto mayor debe tener una edad igual o
# superior a 60. Debe validar para cada ingreso, que los valores estén en un rango entre 1 y 120 años.
# En caso de error deberá notificar y solicitar un nuevo valor

edades = []
persona = 1

while True:
    try:
        ingresar_edad = int(input(f"Ingrese la edad de la persona número {persona}: "))
        #validaciones de rango de edad
        if ingresar_edad < 0:
            print("Error: la edad no puede ser un número negativo. Intente de nuevo.")
            continue  
        if ingresar_edad > 120:
            print("Error: la edad no puede superar el limite de 120 años. Intente de nuevo.")
            continue  
        #guardar edad
        edades.append(ingresar_edad)
        persona += 1
        #limite de personas
        if persona > 10:
            break
    except ValueError:
        print("Error: Ingrese un número entero válido.")
 
        
menor_de_edad = 0
mayor_de_edad  = 0
adulto_mayor = 0

for edades_recorridas in edades:
   #bloque if de determinación de edades
    if edades_recorridas < 18:
        menor_de_edad += 1
    elif edades_recorridas > 18 and edades_recorridas < 60:
        mayor_de_edad += 1
    elif edades_recorridas >= 60 and edades_recorridas <= 120:
        adulto_mayor += 1 
    
     
print(f"En total hay {menor_de_edad} personas menores de edad")
print(f"El total hay {mayor_de_edad} personas mayores de edad")
print(f"El total hay {adulto_mayor} personas adulto mayor")


#Edad mas alta y mas baja
edad_baja =min(edades)       
print (f"la edad mas baja es la de {edad_baja}")
edad_alta = max(edades)
print (f"la edad mas alta es la de {edad_alta}")

#promedio de edades
promedio = sum(edades) / len(edades)
print (f"El promedio de las edades ingresadas en de {promedio}")   


