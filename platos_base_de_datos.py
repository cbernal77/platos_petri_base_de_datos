import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('petri_dishes.db')
c = conn.cursor()

# Eliminar la tabla existente si ya existe
c.execute('DROP TABLE IF EXISTS platos')

# Crear la tabla nuevamente con la columna comentario
c.execute('''
CREATE TABLE IF NOT EXISTS platos (
    id INTEGER PRIMARY KEY,
    tipo_muestra TEXT,
    unidad_almacenamiento TEXT,
    compartimiento TEXT,
    comentario TEXT
)
''')

# Guardar cambios y cerrar la conexión
conn.commit()
conn.close()



def agregar_plato():
    # Solicitar datos al usuario
    id = input("Ingresa el ID del plato: ")
    tipo_muestra = input("Ingresa el tipo de muestra: ")
    unidad_almacenamiento = input("Ingresa la unidad de almacenamiento: ")
    compartimiento = input("Ingresa el compartimiento: ")
    comentario = input("Ingresa un comentario: ")

    #Conectar a la base de datos
    conn = sqlite3.connect("petri_dishes.db")
    c = conn.cursor()

    # Insertar los datos en la tabla
    c.execute('''
    INSERT INTO platos (id, tipo_muestra, unidad_almacenamiento, compartimiento, comentario)
    VALUES (?,?,?,?,?)
    ''', (id, tipo_muestra, unidad_almacenamiento, compartimiento, comentario))

    # Guardar cambios y cerrar la conexion
    conn.commit()
    conn.close()

    print("¡Plato agregado exitosamente!")



def mostrar_platos():
    # Conectar a la base de datos
    conn = sqlite3.connect('petri_dishes.db')
    c = conn.cursor()

    # Consultar todos los platos
    c.execute('SELECT * FROM platos')
    platos = c.fetchall()

    if platos:
        for plato in platos:
            print(f"ID: {plato[0]}, tipo de muestra: {plato[1]}, unidad de almacenamiento: {plato[2]}, compartimiento: {plato[3]}, comentario: {plato[4]} ")
    else:
        print("No hay platos en la base de datos")

    # Cerrar la conexion
    conn.close()



def eliminar_plato():

    id = input("Ingresa el ID del plato a eliminar: ")

    if id:
        # Conectar a la base de datos
        conn = sqlite3.connect('petri_dishes.db')
        c = conn.cursor()

        # Verificar si el ID existe en la base de datos
        c.execute('SELECT * FROM platos WHERE id = ?', (id,))
        plato = c.fetchone()

        if plato:
            # El ID existe, eliminar el plato
            c.execute('DELETE FROM platos WHERE id = ?',(id,))
            conn.commit()
            print(f"Plato con ID {id} eliminado exitosamente.")
        else:
            print("El id no existe en la base de datos")

        # Cerrar la conexion
        conn.close()
    else:
        print("El ID no existe en la base de datos")

def mostrar_menu():

    while True:
        print("\n---Menu---")
        print("1. Agregar plato")
        print("2. Mostrar platos")
        print("3. Eliminar plato")
        print("4. Salir")

        opcion = input("Elija una opcion: ")

        if opcion == "1":
            agregar_plato()
        elif opcion == "2":
            mostrar_platos()
        elif opcion == "3":
            eliminar_plato()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("La opcion no es valida")

# Llamada principal para iniciar el menu
#Al tener mostrar_menu() en este bloque,
# el programa siempre empezará en el menú cuando ejecutes el archivo.
if __name__ == "__main__":
    mostrar_menu()