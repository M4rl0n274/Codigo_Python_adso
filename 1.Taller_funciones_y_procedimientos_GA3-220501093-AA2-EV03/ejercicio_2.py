# Realizar la conversión de una temperatura dada en grados Centígrados a grados Fahrenheit
# (Fórmula: F = (9/5) C + 32).

print("===Conversor de Temperatura===")
print()

while True:
    try:
        print("(1 = Centigrados a Farenheit) o (2 = Farenheit a Centigrados)")
        opcion = int(input("Elija una opción de conversión: "))
        if opcion in (1 , 2):
            print(f"Elegista la opción {opcion}") 
            print()
            break
        else:
            print("Opción invalida. Intente de nuevo.")
    except ValueError:
        print ("Debe ingresar un número valido ")
    
match opcion:
    case 1:
        grados_centigrados = int(input("Ingrese los grados centigrados: "))
        farenheit = grados_centigrados * 9 / 5 + 32
        print (f"El resultado de la conversion a Grados Farenheit es de: {farenheit}")  
        print()
    case 2:
        grados_farenheit = int(input("Ingrese los grados Farenheit: "))
        centigrados = (grados_farenheit - 32) * 5/9
        print (f"El resultado de la conversion a Grados Centigrados es de:{centigrados}") 
        print()
        






