from libreria_operaciones import operacion

anio_nac = int(input("Año de nacimiento: "))
mes_nac = int(input("Mes de nacimiento: "))
dia_nac = int(input("Día de nacimiento: "))

anio_act = int(input("Año actual: "))
mes_act = int(input("Mes actual: "))
dia_act = int(input("Día actual: "))

# Cálculo de edad
edad = operacion(anio_act,anio_nac,'r')

# Verificar si aún no ha cumplido años este año
if mes_act < mes_nac or (mes_act == mes_nac and dia_act < dia_nac):
    edad = edad - 1

# Mostrar resultado
print("La edad actual es:", edad, "años")

