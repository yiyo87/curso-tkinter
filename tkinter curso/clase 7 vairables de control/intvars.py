import tkinter as tk

ventana = tk.Tk()
entero = tk.IntVar(value=42)#variable conel valor 42

print (entero.get())#obtenemos el valor de la variable 

opcion1 = tk.Radiobutton(ventana, text="opcion 1",variable = entero, value=1)#se crean radio boton con opciones
opcion1.pack()
opcion2 = tk.Radiobutton(ventana, text="opcion2",variable = entero, value =2)
opcion2.pack()

def actualizar (*args):#lo que hace esta funcion es que si tiene la variable entero con el valor de 42 que se imprime por consola
    print (entero.get())#y se crea una ventana con 2 opciones y que si eleige una u otra por consola dependiendo de la opcion 
#si es uno u otro #ojo es importante que dentro de la funcion en los parametros es colocar *args si no no toma y sale un error
entero.trace("w",actualizar)

ventana.mainloop()

