import tkinter as tk#se hace la importacion

ventana = tk.Tk()#se crea la ventana

booleano = tk.BooleanVar(value=False)#se asigna un valor verdadero a la variable

casilla = tk.Checkbutton(ventana,text="aceptar",variable=booleano)
casilla.pack()

def actualizar(*args):#esta funcion es que cada vez que se activa o se desactiva la casilla de
    print(booleano.get())#abajo de el checkbox sale por consola si es verdadero o falso

booleano.trace("w",actualizar)

ventana.mainloop()