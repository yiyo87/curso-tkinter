### esto es muy similar a los input dentro de js###

import tkinter as tk

ventana = tk.Tk()
ventana.title("ejemplo label")

etiqueta = tk.Label(ventana,text="lo de abajo es un entry")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.config(fg="white",bg="black",font=("arial",12))
entrada.pack()

entrada.insert(0,"Nombre")
#texto= entrada.get()
#print(texto)

def aplicar_texto():
    texto= entrada.get()
    etiqueta.config(text=texto)
#lo que hace la funcion es que lo que se escriba dentro de entry se coloca arriba en el label de arriba en el fondo reemplaza el label de arriba
boton_aplicar = tk.Button(ventana,text="aplicar texto",command=aplicar_texto)
boton_aplicar.pack()

ventana.mainloop()