import csv
from fpdf import FPDF
import sqlite3
import datetime

# Conectar a la base de datos
conn = sqlite3.connect('petri_dishes.db')
c = conn.cursor()

# Eliminar la tabla existente si ya existe
c.execute('DROP TABLE IF EXISTS platos')

# Crear la tabla nuevamente con la columna comentario
c.execute('''
CREATE TABLE IF NOT EXISTS platos (
    id TEXT PRIMARY KEY,
    tipo_muestra TEXT,
    unidad_almacenamiento TEXT,
    compartimiento TEXT,
    fecha_vencimiento TEXT,
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
    fecha_vencimiento = input("Ingresa la fecha de vencimiento (YYYY-MM-DD): ")
    comentario = input("Ingresa un comentario: ")

    #Validar el formato de la fecha
    try:
        datetime.datetime.strptime(fecha_vencimiento,"%Y-%m-%d" )
    except ValueError:
        print(" La fecha ingresada no es valida. Debe tener el formato YYYY-MM-DD.")
        return

    #Conectar a la base de datos
    conn = sqlite3.connect("petri_dishes.db")
    c = conn.cursor()

    # Insertar los datos en la tabla
    c.execute(''' INSERT INTO platos (id, tipo_muestra, unidad_almacenamiento, compartimiento, fecha_vencimiento, comentario)
    VALUES (?,?,?,?,?,?)
    ''', (id, tipo_muestra, unidad_almacenamiento, compartimiento, fecha_vencimiento, comentario))

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
            print(f"ID: {plato[0]}, tipo de muestra: {plato[1]}, unidad de almacenamiento: {plato[2]}, compartimiento: {plato[3]},, fecha de vencimiento: {plato[4]}, comentario: {plato[5]} ")

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

def actualizar_plato():

    # Conectar con la base de datos
    conn = sqlite3.connect("petri_dishes.db")
    c = conn.cursor()

    # Pedir el ID del plato a actualizar
    id = input("Ingresa el ID del plato a actualizar: ")

    # Verificar si el plato existe
    c.execute('SELECT * FROM platos WHERE id = ?', (id))
    plato = c.fetchone()

    if plato:
        print(f"Plato encontrado: {plato}")
        print("¿Qué desea actualizar?")
        print("1. Solo un campo")
        print("2. Actualizar todos los campos")

        opcion = input("Elija una opcion: ")

        if opcion == "1":
            print("\nCampos disponibles:")
            print("1. Tipo de muestra")
            print("2. Unidad de almacenamiento")
            print("3. Compartimiento")
            print("4. Fecha de vencimiento")

            print("5. Comentario")

            campo = input("Seleccione un campo para actualizar: ")

            if campo == "1":
                nuevo_tipo_muestra = input("Ingrese el nuevo tipo de muestra: ")
                c.execute('UPDATE platos SET tipo_muestra = ? WHERE id = ?', (nuevo_tipo_muestra, id))

            elif campo == "2":
                nuevo_unidad = input("Ingrese la nueva unidad de almacenamiento: ")
                c.execute('UPDATE platos SET unidad_almacenamiento = ? WHERE id = ?', (nuevo_unidad, id))

            elif campo == "3":
                nuevo_compartimiento = input("Ingrese el nuevo compartimiento: ")
                c.execute('UPDATE platos SET compartimiento = ? WHERE id = ?', (nuevo_compartimiento, id))

            elif campo == "4":
                nueva_fecha_vencimiento = input("Ingrese la nueva fecha de vencimiento (YYYY-MM-DD): ")
                c.execute('UPDATE platos SET fecha_vencimiento = ? WHERE id = ?', (nueva_fecha_vencimiento, id))

            elif campo == "5":
                nuevo_comentario = input("Ingrese el nuevo comentario: ")
                c.execute('UPDATE platos SET comentario = ? WHERE id = ?', (nuevo_comentario, id))


            else:
                print("La opcion es no valida, no se realizaron cambios")

        elif opcion == "2":
            print("\n Actualizando todos los campos...")
            nuevo_tipo_muestra = input("Ingrese el nuevo tipo de muestra: ")
            nuevo_unidad = input("Ingresa la nueva unidad: ")
            nuevo_compartimiento = input("Ingresa el nuevo compartimiento: ")
            nueva_fecha_vencimiento = input("Ingresa la nueva fecha de vencimiento: ")
            nuevo_comentario = input("Ingresa el nuevo comentario: ")
            c.execute('''
                UPDATE platos
                SET tipo_muestra = ?, unidad_almacenamiento = ?, compartimiento = ?, fecha_vencimiento = ?, comentario = ?, 
                WHERE id = ? ''',
                      (nuevo_tipo_muestra,nuevo_unidad,nuevo_compartimiento,nueva_fecha_vencimiento,nuevo_comentario, id))
            print("¡Todos los campos han sido actualizados!")
        else:
            print("Opcion no valida.")

        # Guardar cambios
        conn.commit()
    else:
        print(" No se encontro un plato con ese ID.")

    # Cerrar la conexion
    conn.close()

def buscar_plato_por_id():
    # solicitar el Id del usuario
    id = input("Ingresa el ID del plato a buscar: ")

    if id:
        #conectar a la base de datos
        conn = sqlite3.connect('petri_dishes.db')
        c = conn.cursor()

        # Consultar el plato con el ID proporcionado
        c.execute("SELECT * FROM platos WHERE id= ?", (id,))
        plato = c.fetchone() # recupera el primer resultado encontrado

        if plato:
            # Mostrar los detalles del plato encontrado
            print(f"plato encontrado: ID = {plato[0]}, tipo de muestra = {plato[1]}, unidad de almacenamiento = {plato[2]}, compartimiento = {plato[3]}, fecha de vencimiento = {plato[4]}, comentario = {plato[5]}")
        else:
            # Si no se encuentra el plato con el ID ingresado
            print(f"No se encontro el plato con el ID {id}")

        # Cerrar la conexion con la base de datos
        conn.close()

def verificar_vencimientos():
    # Conectar a la base de datos
    conn = sqlite3.connect("petri_dishes.db")
    c = conn.cursor()

    # Obtener la fecha actual
    fecha_actual = datetime.date.today()

    # Consultar todos los platos y sus fechas de vencimiento

    c.execute("SELECT id, tipo_muestra, fecha_vencimiento FROM platos")
    platos = c.fetchall()

    vencidos = []
    for plato in platos:
        if plato[2]:  # Verificar si la fecha de vencimiento no está vacía
            fecha_vencimiento = datetime.datetime.strptime(plato[2], "%Y-%m-%d").date()
            if fecha_vencimiento < fecha_actual:
                vencidos.append(plato)

    # Mostrar los platos vencidos
    if vencidos:
        print("Platos vencidos:")
        for plato in vencidos:
            print(f"""
                ID: {plato[0]}
                Tipo de muestra: {plato[1]}
                Fecha de vencimiento: {plato[2]}
                """)
    else:

        print("\n✅ No hay platos vencidos. Todo está en orden.")

    # Cerrar la conexión
    conn.close()
'''
# funcion para probar datos
def agregar_plato_prueba():
    """
    Agrega platos con fechas de vencimiento para pruebas.
    """
    conexion = sqlite3.connect('petri_dishes.db')
    c = conexion.cursor()

    # Insertar platos con diferentes fechas de vencimiento
    platos_prueba = [
        ("ID003", "Muestra3", "Unidad1", "Comp3", "Comentario3", "2023-12-06"),
        ("ID004", "Muestra4", "Unidad1", "Comp4", "Comentario4", "2024-12-05"),
    ]

    c.executemany("INSERT INTO platos VALUES (?, ?, ?, ?, ?, ?)", platos_prueba)
    conexion.commit()
    print("Platos de prueba agregados.")
    conexion.close()
'''
def generar_reporte_csv():
    # Conexion a la base de datos
    conn = sqlite3.connect("petri_dishes.db")
    c = conn.cursor()

    # Consultar todos los platos
    c.execute('SELECT * FROM platos')
    platos = c.fetchall()

    # Crear o abrit un archivo CSV para guardar los datos
    nombre_archivo = "reporte_platos.csv"
    with open(nombre_archivo, mode = 'w', newline='', encoding='utf-8') as archivo_csv:
        escritor = csv.writer(archivo_csv)

        # Escribir el encabezado
        encabezados = ["ID","Tipo de muestra","Unidad ", "Compartimiento","Fecha de vencimiento","Comentario"]
        escritor.writerow(encabezados)

        # Escribir los datos de los platos
        escritor.writerows(platos)

    # Cerrar la conexion a la base de datos
    conn.close()

    print(f"Reporte generado exitosamente en '{nombre_archivo}'")




def generar_reporte_pdf():

    # Conectar a la base de datos
    conn = sqlite3.connect('petri_dishes.db')
    c = conn.cursor()

    # Obtener los datos de los platos
    c.execute("SELECT * FROM platos")
    platos = c.fetchall()

    # Crear una instancia de FPDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Titulo del documento
    pdf.set_font("Arial", "", 10)  # Fuente Arial, sin estilo, tamaño 16
    pdf.cell(240, 10, txt="Reporte de Platos de Petri", ln=True, align="L")
    pdf.ln(10)  # Espaciado entre el título y los encabezados



    # Encabezados
    encabezados = ["ID", "Tipo de muestra", "Unidad", "Compartimiento","fecha de vencimiento","Comentario"]
    pdf.set_font("Arial", "B", 8)  # Negrita para los encabezados
    cell_width = 30  # Ancho base de celda


    
    # Dibujar los encabezados
    for encabezado in encabezados:
        pdf.cell(cell_width, 10, txt=encabezado, border=1, align="C")
    pdf.ln()



    
    # Agregar datos al PDF
    pdf.set_font("Arial", "", 10)  # Fuente normal para los datos
    for plato in platos:
        for i, dato in enumerate(plato):
            if i == 5:  # Si es el comentario, usamos multi_cell
                pdf.multi_cell(cell_width, 10, txt=str(dato), border=1, align="C")  # Comentarios largos
            else:
                pdf.cell(cell_width, 10, txt=str(dato), border=1, align="C")
        pdf.ln(5)  # Espaciado entre las filas de datos


    # Guardar el archivo PDF
    nombre_archivo = "reporte_platos.pdf"
    pdf.output(nombre_archivo)
    print(f"Reporte generado y guardado como {nombre_archivo}")


# Llamar a la función para generar el reporte
generar_reporte_pdf()

'''
#funcion para ver la estructura y tipos de datos de la tabla
def verificar_estructura_tabla():
    conexion = sqlite3.connect('petri_dishes.db')
    c = conexion.cursor()

    c.execute("PRAGMA table_info(platos);")
    estructura = c.fetchall()
    print("Estructura de la tabla platos:")
    for columna in estructura:
        print(columna)

    conexion.close()

'''
def mostrar_menu():

    while True:
        print("\n---Menu---")
        print("1. Agregar plato")
        print("2. Mostrar platos")
        print("3. Eliminar plato")
        print("4. Actualizar plato")
        print("5. Buscar Plato por ID")
        print("6. Vencimiento de platos")
        print("7. Generar Reporte (CSV)")
        print("8. Generar Reporte (PDF)")
        print("9. Salir")

        opcion = input("Elija una opcion: ")

        if opcion == "1":
            agregar_plato()
        elif opcion == "2":
            mostrar_platos()
        elif opcion == "3":
            eliminar_plato()
        elif opcion == "4":
            actualizar_plato()
        elif opcion == "5":
            buscar_plato_por_id()
        elif opcion == "6":
            verificar_vencimientos()
        elif opcion == "7":
            generar_reporte_csv()
        elif opcion == "8":
            generar_reporte_pdf()

        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("La opcion no es valida")

# Llamada principal para iniciar el menu
#Al tener mostrar_menu() en este bloque,
# el programa siempre empezará en el menú cuando ejecutes el archivo.
if __name__ == "__main__":
    #verificar_estructura_tabla() llama esta funcion para prueba
    #agregar_plato_prueba()# llama esta funcion para prueba
    mostrar_menu()