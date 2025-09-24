def operacion(operando_uno_func, operando_dos_func, operador_func):
    if operador_func == 's':
        resultado = operando_uno_func + operando_dos_func
        return resultado
    elif operador_func == 'r':
        resultado = operando_uno_func - operando_dos_func
        return resultado
    else:
        return 0
