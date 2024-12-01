# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 14:42:01 2024

@author: fbac7
"""
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import os



platos = []

# Cargar los platos desde el archivo JSON (si existe)
def cargar_platos():
    global platos
    if os.path.exists("platos.json"):
        with open("platos.json", "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        return []

# Guardar los platos en el archivo JSON
def guardar_platos_en_json():
    with open("platos.json", "w", encoding="utf-8") as f:
        json.dump(platos, f, ensure_ascii=False, indent=4)
    print("Platos guardados en el archivo JSON.")

# Lista global de platos
platos = cargar_platos()  # Cargamos los platos desde el archivo al inicio

def agregar_plato():
    # Obtener los datos ingresados por el usuario en los campos de entrada
    id_plato = entry_id.get()  # ID del plato
    unidad = entry_unidad.get()  # Unidad de almacenamiento del plato
    compartimiento = entry_compartimiento.get()  # Compartimiento donde se encuentra el plato
    # Verificar si el ID es único
    for plato in platos:
        if plato["ID"] == id_plato:
            messagebox.showerror("Error",f" el ID '{id_plato}' ya esta en uso, por favor elige otro")
            return # Salir de la función si el ID ya existe

    
    # Verificar que todos los campos estén llenos
    if id_plato and unidad and compartimiento:
        # Si los campos están completos, agregamos el plato a la lista 'platos'
        platos.append({
            "ID": id_plato,
            "Unidad de almacenamiento": unidad,
            "Compartimiento": compartimiento
        })
        
        # Guardar el nuevo plato en el archivo JSON
        guardar_platos_en_json()  # Actualizar el archivo JSON después de agregar un plato
        
        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", "Plato agregado correctamente")


        # Limpiar los campos de entrada para que el usuario pueda agregar otro plato
        limpiar_campos()
    else:
        messagebox.showerror("Error", "Por favor, complete todos los campos")


def limpiar_campos():
    entry_id.delete(0, tk.END)
    entry_unidad.delete(0, tk.END)
    entry_compartimiento.delete(0, tk.END)

# Función para editar los datos de un plato existente
def editar_plato():
    # Obtener el ID del plato que se desea editar
    id_plato = entry_id.get()
    
    if not id_plato:
        messagebox.showerror("Error", "Por favor, ingrese un ID para editar")
        return
    
    # Buscar si el plato con el ID ingresado existe en la lista de platos
    for plato in platos:
        if plato['ID'] == id_plato:
            # Si se encuentra el plato, se obtiene y guarda en variables los nuevos valores ingresados
            nuevo_unidad = entry_unidad.get()
            nuevo_compartimiento = entry_compartimiento.get()

            # Verificar si se ingresaron nuevos valores para unidad de almacenamiento y compartimiento
            if nuevo_unidad:
                plato['Unidad de almacenamiento'] = nuevo_unidad  # Actualizar la unidad de almacenamiento
            if nuevo_compartimiento:
                plato['Compartimiento'] = nuevo_compartimiento  # Actualizar el compartimiento

            # Guardar los cambios en el archivo JSON
            guardar_platos_en_json()  # Actualizar el archivo JSON después de la edición
            
            # Mostrar un mensaje de éxito indicando que el plato fue editado correctamente
            messagebox.showinfo("Éxito", "Plato editado correctamente")
            limpiar_campos()  # Limpiar los campos de entrada después de la edición
            return  # Terminar la función si se encontró y editó el plato
    
    # Si el plato con el ID ingresado no se encuentra en la lista, mostrar un mensaje de error
    messagebox.showerror("Error", "No se encontró un plato con ese ID")

# Función para mover un plato
def mover_plato():
    # Obtener los valores de los campos
    id_plato = entry_id.get()
    nueva_unidad = entry_unidad.get()
    nuevo_compartimiento = entry_compartimiento.get()

    # Verificar que el ID esté ingresado
    if not id_plato:
        messagebox.showerror("Error", "Por favor, ingrese el ID del plato a mover.")
        return

    # Buscar el plato por ID
    for plato in platos:
        if plato['ID'] == id_plato:
            # Actualizar unidad y compartimiento si se ingresaron valores nuevos
            if nueva_unidad:
                plato['Unidad de almacenamiento'] = nueva_unidad
            if nuevo_compartimiento:
                plato['Compartimiento'] = nuevo_compartimiento

            guardar_platos_en_json()  # Guardar los cambios
            messagebox.showinfo("Éxito", "El plato ha sido movido correctamente.")
            limpiar_campos()
            return
    
    # Si no se encuentra el ID
    messagebox.showerror("Error", "No se encontró un plato con ese ID.")



# Función para eliminar un plato de la lista
def eliminar_plato():
    # Obtener el ID del plato que se desea eliminar
    id_plato = entry_id.get()
    
    # Buscar si el plato con el ID ingresado existe en la lista de platos
    for plato in platos:
        if plato['ID'] == id_plato:
            # Si se encuentra el plato, se elimina de la lista de platos
            platos.remove(plato)
            
            # Mostrar un mensaje de éxito indicando que el plato fue eliminado correctamente
            messagebox.showinfo("Éxito", "Plato eliminado correctamente")
            
            # Guardar los cambios en el archivo JSON
            guardar_platos_en_json()  # Actualizar el archivo JSON después de la eliminación
            
            limpiar_campos()  # Limpiar los campos de entrada después de eliminar el plato
            return  # Terminar la función una vez que el plato ha sido eliminado
    
    # Si el plato con el ID ingresado no se encuentra en la lista, mostrar un mensaje de error
    messagebox.showerror("Error", "No se encontró un plato con ese ID")

# Función para buscar un plato en la lista por su ID
def buscar_plato():
    # Obtener el ID del plato que el usuario desea buscar
    id_plato = entry_id.get()
    
    # Verificar si el campo de ID no está vacío
    if id_plato:
        # Recorrer la lista de platos en busca del plato con el ID ingresado
        for plato in platos:
            if plato['ID'] == id_plato:
                # Si se encuentra el plato, mostrar la información del plato encontrado
                messagebox.showinfo(
                    "Plato Encontrado",  # Título del mensaje emergente
                    f"ID: {plato['ID']}\n"
                    f"Unidad de almacenamiento: {plato['Unidad de almacenamiento']}\n"
                    f"Compartimiento: {plato['Compartimiento']}"
                )
                return  # Terminar la función después de mostrar la información

        # Si no se encuentra el plato en la lista, mostrar un mensaje de error
        messagebox.showerror("Error", "No se encontró un plato con ese ID")
    else:
        # Si el campo ID está vacío, mostrar un mensaje de error pidiendo al usuario que ingrese un ID
        messagebox.showerror("Error", "Por favor, ingrese un ID para buscar")
        
def buscar_plato_por_unidad():
    
    unidad = entry_unidad.get()
    if unidad:
    
        for plato in platos:
            
            
            if plato['Unidad de almacenamiento'] == unidad:
                
                messagebox.showinfo(
                    "Plato Encontrado",  # Título del mensaje emergente
                    f"ID: {plato['ID']}\n"
                    f"Unidad de almacenamiento: {plato['Unidad de almacenamiento']}\n"
                    f"Compartimiento: {plato['Compartimiento']}"
            )
                return  # Terminar la función después de mostrar la información

        messagebox.showerror("Error","No se encuentra el plato en esa unidad")
    else:
        # Si el campo ID está vacío, mostrar un mensaje de error pidiendo al usuario que ingrese un ID
        messagebox.showerror("Error", "Por favor, ingrese una unidad para buscar")
    
           
def buscar_plato_por_compartimiento():
    # Obtener el valor del campo de compartimiento
    compartimiento = entry_compartimiento.get()
    
    if compartimiento:  # Verificar que el campo no esté vacío
        # Buscar platos que coincidan con el compartimiento especificado
        for plato in platos:
            if plato['Compartimiento'] == compartimiento:
                # Mostrar información del plato encontrado
                messagebox.showinfo(
                    "Plato Encontrado",
                    f"ID: {plato['ID']}\n"
                    f"Unidad de almacenamiento: {plato['Unidad de almacenamiento']}\n"
                    f"Compartimiento: {plato['Compartimiento']}"
                )
                return  # Terminar la función tras encontrar el primer plato
        
        # Si no se encuentra ningún plato en ese compartimiento
        messagebox.showerror("Error", "No se encontró ningún plato en ese compartimiento.")
    else:
        # Mostrar un mensaje de error si el campo está vacío
        messagebox.showerror("Error", "Por favor, ingrese un compartimiento para buscar.")
'''
def mostrar_platos():
    if platos:
        # Construir el texto de todos los platos, incluyendo el comentario
        platos_texto = "\n".join([
            f"ID: {plato['ID']}, Unidad: {plato['Unidad de almacenamiento']}, "
            f"Compartimiento: {plato['Compartimiento']}"
            for plato in platos
        ])
        # Mostrar la información en un messagebox
        messagebox.showinfo("Platos", platos_texto)
    else:
        # Mensaje si no hay platos registrados
        messagebox.showinfo("Sin platos", "No hay platos registrados")
'''
def mostrar_platos():
    if platos:
        platos_texto = ""
        for plato in platos:
            comentario = plato.get('comentario', 'Sin comentario')  # Si no tiene comentario, muestra un texto por defecto
            platos_texto += f"ID: {plato['ID']}, Unidad: {plato['Unidad de almacenamiento']}, Compartimiento: {plato['Compartimiento']}, Comentario: {comentario}\n"
        messagebox.showinfo("Platos registrados", platos_texto)
    else:
        messagebox.showinfo("Sin platos", "No hay platos registrados")
# Función para actualizar el comentario
'''
def mostrar_platos():
    if platos:
        platos_texto = "\n".join([f"ID: {plato['ID']}, Unidad: {plato['Unidad de almacenamiento']}, Compartimiento: {plato['Compartimiento']}" for plato in platos])
        messagebox.showinfo("Platos", platos_texto)
    else:
        messagebox.showinfo("Sin platos", "No hay platos registrados")
'''
# Función para agregar comentario
def agregar_comentario(id_plato, comentario):
    for plato in platos:
        if plato['ID'] == id_plato:
            plato['comentario'] = comentario
            messagebox.showinfo("Comentario actualizado", f"Comentario del plato con ID {id_plato} actualizado.")
            return
    messagebox.showinfo("Plato no encontrado", f"No se encontró un plato con ID {id_plato}.")

# Función para abrir la ventana emergente donde se agrega el comentario
def abrir_ventana_comentario():
    # Obtener el ID dinámicamente desde el campo de entrada
        id_plato = entry_id.get()
        if not id_plato:
            messagebox.showinfo("Error", "Por favor ingrese un ID válido.")
            return
        ventana_comentario = tk.Toplevel(root)  # Crear ventana emergente
        ventana_comentario.title(f"Actualizar Comentario para ID {id_plato}")
        ventana_comentario.geometry("400x200")

    # Etiqueta y campo de entrada para el comentario
        label_comentario = tk.Label(ventana_comentario, text="Nuevo comentario:")
        label_comentario.pack()
        entry_comentario = tk.Entry(ventana_comentario)
        entry_comentario.pack()

    # Función que actualiza el comentario cuando el usuario lo ingresa
        def actualizar_comentario():
            nuevo_comentario = entry_comentario.get()
            if nuevo_comentario:
                agregar_comentario(id_plato, nuevo_comentario)
                ventana_comentario.destroy()  # Cerrar la ventana emergente
            else:
                messagebox.showinfo("Error", "Por favor ingrese un comentario.")

    # Botón para guardar el comentario
        btn_guardar = tk.Button(ventana_comentario, text="Guardar Comentario", command=actualizar_comentario)
        btn_guardar.pack() # También añadido espacio entre widgets

# Función para agregar el botón de "Agregar Comentario" en la interfaz
def agregar_boton_comentario():
    btn_comentar = tk.Button(root, text= "Agregar Comentario", command=abrir_ventana_comentario) # Llamar a abrir_ventana_comentario directamente
    canvas.create_window(260, 380, window=btn_comentar)

def eliminar_comentario():

    id_plato = entry_id.get()
    if not id_plato:
        messagebox.showinfo("Error","Por favor un Id valido")
        return

    for plato in platos:
        if plato["ID"] == id_plato:
            if 'comentario' in plato:
                del plato['comentario']
                messagebox.showinfo("eliminar comentario","El comentario ha sido eliminado exitosamente")
            else:
                messagebox.showinfo("sin comentario", f"el plato con ID {id_plato} no tiene comentario")
            return
    messagebox.showinfo("plato no encontrado", f"no se encontro un plato con ID {id_plato}")



def confirmar_salir():
    respuesta = messagebox.askyesno("Confirmar salida", "¿Está seguro de que quiere salir?")
    if respuesta:
        root.destroy()


def interfaz_grafica():
    global root,canvas
    root = tk.Tk()
    root.title("Gestión de platos de Petri")
    root.geometry("600x400")
    root.config(bg="#F8DE7E")


    # Crear un Canvas dentro de la ventana principal
    canvas = tk.Canvas(root, width=600, height=400, bg="#F8DE7E")
    canvas.pack(fill="both", expand=True)
    
    # Cargar la imagen del refrigerador
    try:
        image_path = r"C:\Users\fbac7\.spyder-py3\cursopython\imagen\fridge.png"
        image = Image.open(image_path)
        image = image.resize((300, 300))  # Ajusta el tamaño
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(400, 200, image=photo)  
    except FileNotFoundError as e:
        print(f"Error: {e}. No se pudo encontrar la imagen.")
    except Exception as e:
        print(f"Se produjo un error al cargar la imagen: {e}")

    # Crear widgets dentro del Canvas
    global entry_id, entry_unidad, entry_compartimiento
    label1 = tk.Label(root, text="Id", bd=4, relief="groove")
    entry_id = tk.Entry(root)
    entry_id.config(bg="#A5D6A7", bd=3, relief="solid", fg="#333333", highlightthickness=1)
    canvas.create_window(400, 80, window=label1)
    canvas.create_window(400, 120, window=entry_id)

    
    label2 = tk.Label(root, text="Unidad de almacenamiento", bd=4, relief="groove")
    entry_unidad = tk.Entry(root)
    entry_unidad.config(bg="#FFF9C4", bd=3, relief="solid", fg="#333333", highlightthickness=1)
    canvas.create_window(400, 180, window=label2)
    canvas.create_window(400, 220, window=entry_unidad)

    label3 = tk.Label(root, text="Compartimiento", bd=4, relief="groove")
    entry_compartimiento = tk.Entry(root)
    entry_compartimiento.config(bg="#B3E5FC", bd=3, relief="solid", fg="#333333", highlightthickness=1)
    canvas.create_window(400, 260, window=label3)
    canvas.create_window(400, 300, window=entry_compartimiento)

    # Botones para agregar, editar, eliminar, buscar y mostrar platos
    btn_agregar = tk.Button(root, text="Agregar plato", command=agregar_plato)
    btn_editar = tk.Button(root, text="Editar plato", command=editar_plato)
    btn_eliminar = tk.Button(root, text="Eliminar plato", command=eliminar_plato)
    btn_buscar = tk.Button(root, text="Buscar plato", command=buscar_plato)
    button_buscar_plato_por_unidad = tk.Button(root, text="Buscar por Unidad", bd=5, relief="raised", command=buscar_plato_por_unidad)
    button_buscar_plato_por_compartimiento = tk.Button(root, text="Buscar por compartimiento", bd=5, relief="raised", command=buscar_plato_por_compartimiento)
    
    btn_mostrar = tk.Button(root, text="Mostrar platos", command=mostrar_platos)
    btn_salir = tk.Button(root, text="Salir", command=confirmar_salir)
    
    # En la interfaz gráfica:
    button_mover = tk.Button(root, text="Mover plato (Solo laboratorista)", bd=5, relief="raised", command=mover_plato)

    btn_eliminar_comentario = tk.Button(root, text="eliminar comentario", command=eliminar_comentario)
    canvas.create_window(400, 380,window = btn_eliminar_comentario)


    canvas.create_window(150, 60, window=btn_agregar)
    canvas.create_window(150, 100, window=btn_mostrar)
    canvas.create_window(150, 140, window=btn_editar)
    canvas.create_window(150, 180, window=btn_buscar)
    canvas.create_window(150, 220, window=button_buscar_plato_por_unidad)
    canvas.create_window(150, 260, window=button_buscar_plato_por_compartimiento)
    canvas.create_window(150, 300, window=btn_eliminar)
    canvas.create_window(150, 340, window=button_mover)
    canvas.create_window(150, 380, window=btn_salir)

    agregar_boton_comentario()
    root.mainloop()
if __name__ == "__main__":
# Iniciar la interfaz gráfica
    interfaz_grafica()