import tkinter as tk

from tkinter import filedialog

ventana = tk.Tk()
ventana.withdraw()

file_path = filedialog.askopenfilenames()# entrega la ruta del archivo seleccionado mas de un archivo

print (file_path)

#al seleccionar un archivo entrega la ruta o direccion del archivo