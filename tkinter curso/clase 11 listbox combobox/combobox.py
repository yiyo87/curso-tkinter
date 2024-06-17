import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()#se crea la ventana
ventana.title("ejemplo de combobox")#se da titulo a la ventana

combobox = ttk.Combobox(ventana,width=30,font=("Arial",12),foreground="blue",background="white")# se dan propiedades a la ventana
combobox.pack()

elementos = ["elemento 1","elemento 2","elemento 3"]#se crea una lista de elementos
combobox["values"] = elementos#se da valor a los elementos de la lista 

def on_seleccionar(event):#esta funcion permite que dentro de las opciones del menu al momento de elegir una de ellas aparesca por pantalla la que seleccionaste
    valor_seleccionado = combobox.get()
    print(f"seleccionado :{valor_seleccionado}")

combobox.bind("<<ComboboxSelected>>",on_seleccionar)
ventana.mainloop()