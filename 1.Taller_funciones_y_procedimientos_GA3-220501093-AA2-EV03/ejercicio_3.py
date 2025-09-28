# Escribir el algoritmo que permite calcular la nota correspondiente al primer parcial de “análisis”
# para un estudiante cualquiera. Se debe considerar que hay dos talleres y un quiz, que en conjunto
# valen un 30 % de la nota y el resto (70 %) corresponde a la nota del examen parcial.

print("Bienvenido, aqui podra calcular la nota correspondiente al primer parcial de Análisis")
print("Para comenzar ingrese las notas (números de 1 a 5)")



nota_taller = float (input("Ingrese la nota del taller 1: "))
nota_taller_dos = float (input("Ingrese la nota del taller 2: "))
nota_quiz = float (input("Ingrese la nota del Quiz: "))
nota_examen = float (input("Ingrese la nota del Examen: "))
 
prom_taller_quiz = (nota_taller + nota_taller_dos + nota_quiz) /3

nota_final = prom_taller_quiz * 0.30 + nota_examen * 0.70

print(f"La nota final es_ {nota_final:.2f}")

