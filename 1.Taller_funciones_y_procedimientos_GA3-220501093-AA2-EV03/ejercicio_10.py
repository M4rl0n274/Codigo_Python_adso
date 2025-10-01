# Realizar un algoritmo que muestre por pantalla la tabla de multiplicar decreciente de cualquier
# número, ingresado entre el 1 y el 10


while True:
    try:
        num = int(input("Ingrese un número entre 1 y 10: "))
        if not (1 <= num <= 10):
            print("Error: El número debe estar entre 1 y 10.")
            continue
        break
    except ValueError:
        print("Error: Ingrese un número entero válido.")

print(f"\nTabla de multiplicar decreciente del {num}:\n")

for i in range(10, 0, -1):  
    print(f"{num} x {i} = {num * i}")

