#lista vacia para almacenar los contactos
contactos = []

#funcion para agregar un contacto si no existe
def agregar_contacto(nombre,telefono,correo):

    #verifica si el nombre ya existe
    for contacto in contactos:
            print(f"El contacto con el nombre {nombre} ya existe")
            return # no agregar el contacto si ya existe

    #si no existe ,crear un diccionsrio con los datos del contacto
    contacto = {

        "nombre": nombre,
        "telefono": telefono,
        "correo": correo
    }

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