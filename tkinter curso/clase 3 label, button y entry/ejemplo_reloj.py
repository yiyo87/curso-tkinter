import time
import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo label")

etiqueta = tk.Label(ventana, text="hola, soy un label")#dentro de la ventana creo un label y con un texto en el
etiqueta.pack()

def actualizar_hora():
    etiqueta.config(text=time.strftime("%H:%M:%S"))#con el metodo config se puede cambiar el texto de una variable o etiqueta 
    ventana.after(1000,actualizar_hora)#en este caso de ser hola, soy un label pasa a ser un reloj
    #esta funcion after va a ajecutar una accion cada determinado segundos

actualizar_hora()

ventana.mainloop()