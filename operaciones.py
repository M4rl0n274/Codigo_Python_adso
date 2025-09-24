print("Este programa le permite realizar operaciones entre dos operandos")
operando_uno = int(input("Por favor ingrese el primer operando"))
operando_dos = int(input("Por favor ingrese el segundo operando"))
operador = input("Por favor ingrese la operacion deseada (SUMA:S - RESTA:R)")


def operacion(operando_uno_func, operando_dos_func, operador_func):
    if operador_func == 's':
        resultado = operando_uno_func + operando_dos_func
        return resultado
    elif operador_func == 'r':
        resultado = operando_uno_func - operando_dos_func
        return resultado
    else:
        return 0

print("el resultado de la operacion es: ", operacion(operando_uno, operando_dos, operador))