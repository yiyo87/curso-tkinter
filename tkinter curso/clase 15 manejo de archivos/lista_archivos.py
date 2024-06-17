import os
import tkinter as tk
from tkinter import filedialog

def seleccionar_directorio():
    dir_path = filedialog.askdirectory()#metodo cuando seleccione una carpeta y 
    if dir_path:
        listbox.delete(0,tk.END)
        for file in os.listdir(dir_path):
            listbox.insert(tk.END,file)

ventana = tk.Tk()
ventana.title("navegador de archivos")

listbox = tk.Listbox(ventana)
listbox.pack(expand=True,fill="both")

seleccionar_button = tk.Button(ventana,text="seleccionar directorio",command=seleccionar_directorio)
seleccionar_button.pack()

ventana.mainloop()