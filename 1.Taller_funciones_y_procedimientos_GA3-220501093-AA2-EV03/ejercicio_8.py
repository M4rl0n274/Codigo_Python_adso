# Diseñar un algoritmo que permita ingresar la hora, minutos y segundos, y que calcule la hora en el
# siguiente segundo ("0<= H <=23", "0<= M <=59" "0<= S<=59").

from datetime import datetime, timedelta

while True:
    try:
        H = int(input("Ingrese la hora (0-23): "))
        M = int(input("Ingrese los minutos (0-59): "))
        S = int(input("Ingrese los segundos (0-59): "))

        # Validaciones
        if not (0 <= H <= 23 and 0 <= M <= 59 and 0 <= S <= 59):
            print("Error: La hora debe estar entre 0-23, los minutos y segundos entre 0-59.")
            continue
        break
    except ValueError:
        print("Error: Debe ingresar valores enteros válidos.")


hora_actual = datetime(2025, 1, 10, H, M, S)


hora_siguiente = hora_actual + timedelta(seconds=1)

print("La hora en el siguiente segundo es:", hora_siguiente.strftime("%H:%M:%S"))


