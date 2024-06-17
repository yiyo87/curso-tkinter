import tkinter as tk

from tkinter import filedialog

ventana = tk.Tk()
ventana.withdraw()

file_obj = filedialog.asksaveasfile(mode="a",defaultextension=".txt")
if file_obj:#el metodo para guardar los archivos es asksavesfile
    file_obj.write("hola, mundo")
    file_obj.close()


