import tkinter as tk
from tkinter import Button#importa una funcionalidad a los botones
from tkinter.scrolledtext import ScrolledText#ya sabemos que es para poder hacer scroll dentro de la aplicacion
from tkinter.filedialog import askopenfile, asksaveasfile#se importa estas funciones para poder guardar o abrir documentos 

def abrir_archivo():#las funciones para guardar o abrir archivo que despues mas adelante se van a ocupar dentro del mismo codigo
    archivo = askopenfile()
    if archivo:
        texto_desplazable.delete(1.0, "end")
        with open(archivo.name, "r") as file:
            texto_desplazable.insert(1.0, file.read())

def guardar_archivo():
    archivo = asksaveasfile()
    if archivo:
        with open(archivo.name, "w") as file:
            file.write(texto_desplazable.get(1.0, "end"))

ventana = tk.Tk()
ventana.title("Editor de Texto")

texto_desplazable = ScrolledText(ventana, wrap="word")
texto_desplazable.pack(expand=True, fill="both")

boton_abrir = Button(ventana, text="Abrir", command=abrir_archivo)
boton_abrir.pack(side="left")#estos son los botones que serviran tanto para guardar como para abrir

boton_guardar = Button(ventana, text="Guardar", command=guardar_archivo)
boton_guardar.pack(side="left")

ventana.mainloop()



