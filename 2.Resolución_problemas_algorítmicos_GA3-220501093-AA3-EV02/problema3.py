# Una emisora con presencia en diferentes ciudades, desea conocer el rating de canciones y
# cantantes más escuchados (sonados) en este semestre del año. Por lo tanto, se ha pedido a
# aprendices del SENA desarrollar una solución que permita conocer la respuesta de 6 personas con
# relación a sus gustos musicales. Con fines administrativos y realizar una rifa entre las personas
# encuestadas, la emisora desea poder registrar de las personas entrevistadas su nombre, número de
# identificación (cédula), fecha de nacimiento, correo electrónico, ciudad de residencia, ciudad de
# origen. Además, se deberá poder almacenar el artista y título de hasta 3 canciones favoritas en
# cada una de las personas que se ingrese. Teniendo en cuenta lo anterior, se sugiere que la solución
# deberá mostrar un menú que permita las siguientes opciones:

# a. Agregar una persona con los datos que se listan anteriormente.
# b. Mostrar la información personal de una persona particular por medio de su posición en el
# vector.
#

class Persona:
    def __init__(persona, nombre, cedula, fecha, correo, residencia, origen):
        persona.nombre = nombre
        persona.cedula = cedula
        persona.fecha_nacimiento = fecha
        persona.correo = correo
        persona.ciudad_residencia = residencia
        persona.ciudad_origen = origen
        persona.canciones = []  

    def agregar_cancion(persona, artista, titulo):
        """Agrega una canción favorita (máximo 3)."""
        if len(persona.canciones) < 3:
            persona.canciones.append({"artista": artista, "titulo": titulo})
        else:
            print("Ya se registraron 3 canciones favoritas para esta persona.")

    def mostrar_info(persona):
        """Muestra toda la información de la persona."""
        print("\n--- Información Personal ---")
        print(f"Nombre: {persona.nombre}")
        print(f"Cédula: {persona.cedula}")
        print(f"Fecha de nacimiento: {persona.fecha_nacimiento}")
        print(f"Correo electrónico: {persona.correo}")
        print(f"Ciudad de residencia: {persona.ciudad_residencia}")
        print(f"Ciudad de origen: {persona.ciudad_origen}")
        print("\n--- Canciones Favoritas ---")
        if persona.canciones:
            for i, c in enumerate(persona.canciones, 1):
                print(f"{i}. {c['titulo']} - {c['artista']}")
        else:
            print("Sin canciones registradas.")



personas = []


def agregar_persona():
    """Función para registrar una nueva persona."""
    if len(personas) >= 6:
        print("\nSolo se permiten registrar 6 personas.")
        return

    print("\n--- Registro de Nueva Persona ---")
    nombre = input("Nombre: ")
    cedula = input("Cédula: ")
    fecha = input("Fecha de nacimiento (YYYY-MM-DD): ")
    correo = input("Correo electrónico: ")
    residencia = input("Ciudad de residencia: ")
    origen = input("Ciudad de origen: ")

    persona = Persona(nombre, cedula, fecha, correo, residencia, origen)

    print("\n--- Canciones Favoritas (máx. 3) ---")
    for i in range(3):
        print(f"\nCanción #{i+1}")
        artista = input("Artista: ")
        titulo = input("Título: ")
        persona.agregar_cancion(artista, titulo)

    personas.append(persona)
    print("\n Persona registrada con éxito.")


def mostrar_persona():
    """Función para mostrar la información de una persona por su posición."""
    if not personas:
        print("\n No hay personas registradas.")
        return

    try:
        pos = int(input(f"Ingrese la posición (1 a {len(personas)}): ")) - 1
        if 0 <= pos < len(personas):
            personas[pos].mostrar_info()
        else:
            print("❌ Posición fuera de rango.")
    except ValueError:
        print("❌ Debe ingresar un número válido.")



while True:
    print("\n============================")
    print("     MENÚ DE LA EMISORA     ")
    print("============================")
    print("1. Agregar persona")
    print("2. Mostrar persona por posición")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_persona()
    elif opcion == "2":
        mostrar_persona()
    elif opcion == "3":
        print("\nPrograma finalizado.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
