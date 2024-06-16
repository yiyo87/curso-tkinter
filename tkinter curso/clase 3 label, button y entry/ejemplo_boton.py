import tkinter as tk

ventana = tk.Tk()
ventana.title("mi ventana")

boton = tk.Button(ventana, text="presiona aqui")#clase button
boton.config(fg="white",bg="green",font=("arial",12))
boton.pack()

etiqueta = tk.Label(ventana,text="hola soy un label")
etiqueta.pack()

"""
def boton_presionado():#esta funcion hace que cada vez que presionamos un boton aparece un mensaje por consola que es boton presionado
    print("boton presionado")

boton.config(command=boton_presionado)#esto es lo que hace que el boton tenga accion 
"""

def cambiar_texto():#lo que hace esta funcion es que dentro de una etiqueta el presionar el boton aparece
    etiqueta.config(text="boton presionado")#hace que cambie el mensaje dentro de la ventana y debajo de la etiqueta

boton.config(command=cambiar_texto)


ventana.mainloop()