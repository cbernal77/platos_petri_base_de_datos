import re # Para validar el correo

#lista vacia para almacenar los contactos
contactos = []

# Set para llevar un control eficiente de los nombres ya registrados
"""
Uso del set como única fuente de verdad para verificar duplicados,
lo que hace que el código sea más eficiente. 
El conjunto nombres_registrados garantiza que solo puedas tener un 
contacto con un nombre único (después de normalizarlo).
"""
nombres_registrados = set()

def normalizar_nombre(nombre):
    """normaliza el nombre para evitar duplicados insensibles a mayusculas y minusculas"""
    return nombre.strip().lower() # quito espacios y convierte a minusculas

   #funcion para agregar un contacto si no existe
def agregar_contacto(nombre,telefono,correo):
    # normalizar el nombre
    nombre_normalizado = normalizar_nombre(nombre)

    # verificar si el nombre ya existe (comparando el nombre normalizado)
    if nombre_normalizado in nombres_registrados:
        print(f"El contacto con el nombre '{nombre}' ya existe.")
        return  # no agregar el contacto si ya existe

    """
        validar nombre: no debe estar vacio
        Si el nombre ingresado es " " (solo espacios), nombre.strip()
        se convierte en "" y el if se ejecuta, mostrando el mensaje:
        "El nombre no puede estar vacío."
        Si el nombre ingresado es "Juan", nombre.strip() no cambia nada
        y el if no se ejecuta, por lo que el contacto se agrega.
    """
    if not nombre.strip():
        print("El nombre no puede estar vacio.")
        return

    # validar telefono: debe ser solo numeros y tener entre 7 y 15 caracteres

    if not telefono.isdigit() or not (7 <= len(telefono) <= 15):
        print("El telefono debe contener solo numeros y tener entre 7 y 15 digitos")
        return  # Después de mostrar el mensaje, el return hace que la función se detenga
        # inmediatamente. Esto significa que no se ejecutará más código dentro de esa función
        # y el contacto no será agregado.
        # Sin el return, el código seguiría ejecutándose y agregaría
        # el contacto incluso si el nombre no es válido.
    # validar correo: debe tener el formato esperado

    if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):  # Esto es una expresión regular simple para correos
        print("El correo no tiene un formato válido.")
        return
    '''
    #verifica si el nombre ya existe
    for contacto in contactos:
        if contacto["nombre"].lower() == nombre.lower():
            # convierte todos los caracteres a minúsculas, "Juan" es igual a "juan"
            print(f"El contacto con el nombre {nombre} ya existe")
            return # no agregar el contacto si ya existe
    '''

    #crear un diccionario con los datos del contacto
    contacto = {

        "nombre": nombre,
        "telefono": telefono,
        "correo": correo
    }

    # Guardar el nombre normalizado en el conjunto para futuras verificaciones
    nombres_registrados.add(nombre_normalizado)

    # Agregar el contacto a la lista
    contactos.append(contacto)
    print(f"Contacto {nombre} agregado correctamente")
'''
def editar_contacto(nombre):
    # Normalizar el nombre ingresado para comparar con los registros existentes
    nombre_normalizado = normalizar_nombre(nombre)
    # Recorrer la lista de contactos para encontrar el contacto que se quiere editar

    if not contactos:
        print("No hay contactos para editar")
        return

    for contacto in contactos:
        # Verificar si el contacto actual tiene el mismo nombre (ignorando mayúsculas/minúsculas)
        if normalizar_nombre(contacto['nombre']) == nombre_normalizado:
            print(f"contacto encontrado: {contacto}") # Mostrar el contacto actual

            # Actualizar el conjunto de nombres registrados para reflejar el cambio de nombre
            # Eliminar el nombre antiguo del conjunto
            nombres_registrados.remove(normalizar_nombre(contacto["nombre"]))

            # Solicitar al usuario los nuevos valores para el contacto
            contacto["nombre"] = input("Nuevo nombre: ")
            contacto["telefono"] = input("Nuevo telefono: ")
            contacto["correo"] = input("Nuevo correo: ")

            # Agregar el nuevo nombre al conjunto
            nombres_registrados.add(normalizar_nombre(contacto["nombre"]))  # Agregar el nuevo nombre

            print("Contacto actualizado") # Confirmación de la actualización
            return # Finaliza la función después de actualizar el contacto

        # Si no se encuentra el contacto, mostrar un mensaje
        print("Contacto no encontrado")

'''
def editar_contacto(nombre):
    """
    Editar teléfono y correo de un contacto existente.
    Permitir cambio de nombre solo con confirmación explícita.
    """
    if not contactos:
        print("No hay contactos para editar.")  # Validar si la lista está vacía
        return

    # Normalizar el nombre ingresado para comparar con los registros existentes
    nombre_normalizado = normalizar_nombre(nombre)

    # Buscar el contacto en la lista
    for contacto in contactos:
        if normalizar_nombre(contacto['nombre']) == nombre_normalizado:
            print(f"Contacto encontrado: {contacto}")  # Mostrar el contacto actual

            # Solicitar nuevo teléfono (opcional)
            nuevo_telefono = input("Nuevo teléfono (dejar en blanco para no cambiar): ")
            if nuevo_telefono:
                contacto["telefono"] = nuevo_telefono

            # Solicitar nuevo correo (opcional)
            nuevo_correo = input("Nuevo correo (dejar en blanco para no cambiar): ")
            if nuevo_correo:
                contacto["correo"] = nuevo_correo

            # Preguntar si desea cambiar el nombre
            cambiar_nombre = input("¿Desea cambiar el nombre del contacto? (s/n): ").lower()
            if cambiar_nombre == "s":
                nuevo_nombre = input("Nuevo nombre: ")
                confirmar_nombre = input(f"¿Está seguro de cambiar el nombre a '{nuevo_nombre}'? (s/n): ").lower()
                if confirmar_nombre == "s":
                    # Actualizar el conjunto de nombres registrados
                    nombres_registrados.remove(nombre_normalizado)
                    nombres_registrados.add(normalizar_nombre(nuevo_nombre))
                    contacto["nombre"] = nuevo_nombre
                    print("El nombre ha sido cambiado exitosamente.")
                else:
                    print("El nombre no fue cambiado.")
            else:
                print("El nombre no fue cambiado.")

            print("Contacto actualizado.")  # Confirmación de los cambios
            return

    print("Contacto no encontrado.")  # Si no se encuentra el contacto


def mostrar_menu():
    print("\nSeleccione una opcion: ")
    print("1. Agregar un nuevo contacto")
    print("2. Editar un contacto existente")
    print("3. Salir")


def pedir_datos():
    # solicita los datos por pantalla
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el telefono del contacto: ")
    correo = input("Ingrese el correo del contacto: ")

    # llamar a la funcion agregar_contacto con los datos introducidos
    agregar_contacto(nombre, telefono, correo)

def main():
    while True:
        mostrar_menu()
        opcion = input("Opcion: ")

        if opcion == "1":

            pedir_datos()

            # preguntar si desea agregar otro contacto
            continuar = input("desea agregar otro contacto? (s/n): ")

            if continuar.lower() != "s":
                continue

        elif opcion == "2":
            nombre = input("Ingrese el nombre del contacto a editar: ")
            editar_contacto(nombre)
        elif opcion == "3":
            print("Gracias por usar el programa")
            break
        else:
            print("Opcion no valida")
# Iniciar el programa
if __name__ == "__main__":
    main()

    # Mostrar todos los contactos almacenados
print("\nLista de Contactos:")
for contacto in contactos:
    print(contacto)