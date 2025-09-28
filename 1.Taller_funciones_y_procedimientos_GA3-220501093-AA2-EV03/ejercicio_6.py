# Hacer un programa que sume 5 precios de camisas (en dólares) y que luego muestre el total de la
# venta en pesos.

camisas_total_dolar = 0
suma = 0
contador = 0
dolar_actual = 3.893

while True:
    contador += 1
    camisa = float(input("Ingrese el precio de la camisa (en dolares): "))
    suma = suma + camisa
    camisas_total_dolar = suma
    if contador >=5:
        break


total = camisas_total_dolar * dolar_actual
print(f"El total de la venta es de: ${total:.3f} Pesos Colombianos")