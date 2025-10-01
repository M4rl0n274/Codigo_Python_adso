# # Hacer un programa que registre el consumo realizado por los clientes de un restaurante, si el
# # consumo de cada cliente excede 50000 se hará un descuento del 20 %. Se debe mostrar el pago de
# # cada cliente y el total de todos los pagos


total_recaudado = 0.0
contador = 1


while True:
    try:
        n = int(input("Ingrese el número de clientes: "))
        if n <= 0:
            print("El número de clientes debe ser mayor que 0. Intente de nuevo.")
            continue
        break
    except ValueError:
        print("Error: Por favor ingrese un número entero válido.")


for i in range(n):
    while True:
        try:
            consumo = float(input(f"Ingrese el consumo del cliente {contador}: "))
            if consumo < 0:
                print("⚠ El consumo no puede ser negativo. Intente de nuevo.")
                continue
            break
        except ValueError:
            print("⚠ Error: Ingrese un valor numérico válido.")


    if consumo > 50000:
        pago = consumo * 0.80  
        print(f"Cliente {contador}: consumo ${consumo:.2f} → con descuento paga ${pago:.2f}")
    else:
        pago = consumo
        print(f"Cliente {contador}: consumo ${consumo:.2f} → paga ${pago:.2f}")

    total_recaudado += pago
    contador += 1


print(f"\nEl Total recaudado por todos los clientes: ${total_recaudado:.2f}")



