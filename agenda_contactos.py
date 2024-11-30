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

def pedir_datos():
    #solicita los datos por pantalla
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el telefono del contacto: ")
    correo = input("Ingrese el correo del contacto: ")

    #llamar a la funcion agregar_contacto con los datos introducidos
    agregar_contacto(nombre,telefono,correo)

    # bucle para agregar varios contactos
while True:
    pedir_datos()

    # preguntar si desea agregar otro contacto
    continuar = input("desea agregar otro contacto? (s/n): ")

    if continuar.lower() != "s":
        break

    # Mostrar todos los contactos almacenados
print("\nLista de Contactos:")
for contacto in contactos:
    print(contacto)