"""Programa para registrar giros en el Terminal de Roldanillo."""

# La cédula termina en 57, por eso la lista tiene exactamente 57 posiciones.
CAPACIDAD_MAXIMA = 57
giros = [None] * CAPACIDAD_MAXIMA
cantidad_giros = 0


def validar_monto():
    """Solicita un monto hasta recibir un número entero mayor que cero."""
    while True:
        dato = input("Ingrese el monto del giro: $").strip()

        try:
            monto = int(dato)

            if monto > 0:
                break

            print("El monto debe ser mayor que cero.")
        except ValueError:
            print("Entrada inválida. Escriba el monto usando solamente números.")

    return monto


def registrar_giro(lista, posicion):
    """Registra el nombre y el monto de un giro en una posición disponible."""
    if posicion >= len(lista):
        print("No hay espacio disponible para registrar más giros.")
        return False

    while True:
        nombre = input("Ingrese el nombre del destinatario: ").strip()

        if nombre != "":
            break

        print("El nombre no puede quedar vacío.")

    monto = validar_monto()
    lista[posicion] = [nombre, monto]
    print("Giro registrado correctamente.")
    return True


def listar_giros(lista, cantidad):
    """Muestra todos los giros que han sido registrados."""
    if cantidad == 0:
        print("Todavía no hay giros registrados.")
        return

    print("\n--- GIROS REGISTRADOS ---")
    i = 0

    while i < cantidad:
        nombre = lista[i][0]
        monto = lista[i][1]
        print(f"{i + 1}. {nombre} - ${monto:,}")
        i = i + 1


def buscar_por_nombre(lista, cantidad):
    """Busca coincidencias sin diferenciar mayúsculas y minúsculas."""
    if cantidad == 0:
        print("Todavía no hay giros registrados.")
        return

    nombre_buscado = input("Nombre que desea buscar: ").strip().lower()
    encontrado = False
    i = 0

    while i < cantidad:
        nombre_registrado = lista[i][0].lower()

        if nombre_buscado in nombre_registrado:
            print(f"Coincidencia: {lista[i][0]} - ${lista[i][1]:,}")
            encontrado = True

        i = i + 1

    if not encontrado:
        print("No se encontraron giros con ese nombre.")


def calcular_total_recursivo(lista, indice):
    """Suma recursivamente los montos desde el índice indicado."""
    # Caso base: se llegó al final de los giros registrados.
    if indice == len(lista):
        return 0

    # Cada llamada suma un monto y avanza a la siguiente posición.
    return lista[indice][1] + calcular_total_recursivo(lista, indice + 1)


def mostrar_menu():
    """Imprime las opciones disponibles."""
    print("\n=== TERMINAL DE TRANSPORTES DE ROLDANILLO ===")
    print("1. Registrar giro")
    print("2. Mostrar total de giros")
    print("3. Listar giros")
    print("4. Buscar por nombre")
    print("5. Salir")


# El menú se repite hasta que el usuario selecciona la opción de salida.
opcion = ""

while opcion != "5":
    mostrar_menu()
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        if registrar_giro(giros, cantidad_giros):
            cantidad_giros = cantidad_giros + 1
    elif opcion == "2":
        # Solo se envían a la función las posiciones que contienen giros.
        giros_registrados = giros[:cantidad_giros]
        total = calcular_total_recursivo(giros_registrados, 0)
        print(f"El total de los giros es: ${total:,}")
    elif opcion == "3":
        listar_giros(giros, cantidad_giros)
    elif opcion == "4":
        buscar_por_nombre(giros, cantidad_giros)
    elif opcion == "5":
        print("Gracias por utilizar el sistema.")
        
    else:
        print("Opción inválida. Seleccione un número del 1 al 5.")
