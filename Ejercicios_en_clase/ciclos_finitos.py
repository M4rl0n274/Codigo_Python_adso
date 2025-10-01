print("Este programa imprime los numero consecutivos segun sus indicaciones.")
inicio= int(input("En que numero quiere iniciar: "))
repeticiones = int(input("Cuantas veces quiere que se repita el ciclo: "))

for i in range(inicio, repeticiones + inicio + 1):
    print (i)