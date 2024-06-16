import tkinter as tk

ventana = tk.Tk()  # esta variable es para crear una ventana

texto = tk.StringVar(value="hola, mundo")  # se crea una variable de tipo string con el hola mundo

print(texto)

entrada = tk.Entry(ventana, textvariable=texto)  # dentro de la ventana se crea una input o entry que se llama en tkinter donde se puedo escribir 
entrada.pack()

etiqueta = tk.Label(ventana)  # dentro de la ventana creo un label y con un texto en el
etiqueta.pack()

def actualizar_etiqueta(*args):#lo que hace esta funcion es que toma la etiqueta y lo que tiene dentro de la etiqueta y si se genera alguin cambio lo muestra abajo de esa etiqueta
    etiqueta.config(text=texto.get())

texto.trace("w", actualizar_etiqueta)  # Pasar la referencia a la función sin paréntesis

print(texto.get())
ventana.mainloop()  # esto sirve para que la ventana no se cierre por si sola