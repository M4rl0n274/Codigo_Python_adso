#Dado N, escribir el producto desde 1 hasta N.

while True:
    try:
        N = int(input("¿Hasta que Número desa llegar?: "))
        if N <= 0:
            print ("Error: El número digitado debe ser mayor a cero")
            continue
        break

    except ValueError:
        print ("Error: debe ingresar un número entero")

producto = 1
for i in range(1, N + 1):
    producto *= i
    
print(f"El producto desde 1 hasta {N} es: {producto}")