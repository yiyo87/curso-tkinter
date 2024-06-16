import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo Label")

etiqueta = tk.Label(ventana,text="hola, soy un label")
etiqueta.config(fg="blue",bg="yellow",font=("arial",12,"bold"))
etiqueta.pack()

ventana.mainloop()