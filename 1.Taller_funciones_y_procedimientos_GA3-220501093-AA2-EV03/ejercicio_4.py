#Un capital C está situado a un tipo de interés R anual ¿al término de cuántos años se doblará?

import math


R = float(input("Ingrese la tasa de interés anual (en %): ")) / 100  # convertir a decimal


if R > 0:
    t_compuesto = math.log(2) / math.log(1 + R)
    print(f"Con interés compuesto el capital se duplicará en aproximadamente {t_compuesto:.2f} años.")
else:
    print("La tasa de interés debe ser mayor a 0 para interés compuesto.")


if R > 0:
    t_simple = 1 / R
    print(f"Con interés simple el capital se duplicará en aproximadamente {t_simple:.2f} años.")
