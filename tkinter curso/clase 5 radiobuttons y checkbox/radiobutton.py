import tkinter as tk

ventana = tk.Tk()
ventana.title = ("ejemplo radiobutton")

variable_control= tk.IntVar()

opcion1 = tk.Radiobutton(ventana,text="Opcion 1",variable=variable_control,value=1)
opcion2 = tk.Radiobutton(ventana,text="Opcion 2",variable=variable_control,value=2)

opcion1.pack()
opcion2.pack()

def mostrar_seleccion():
    print("Opcion seleccionada:",variable_control.get())

boton= tk.Button(ventana, text="Mostrar seleccion",command=mostrar_seleccion)
boton.pack()
#lo que hace esta funcion es que dependiendo de la seleccion que hagamos aparece por consola un mensaje mostrando la seleccion que es esta eligiendo 

def cambiar_color():
    color_seleccionado = variable_control.get()
    if color_seleccionado ==1:
        ventana.config(bg="red")
    elif color_seleccionado ==2:
        ventana.config(bg="blue")

opcion1 = tk.Radiobutton(ventana,text="Rojo",variable=variable_control,value=1,command=cambiar_color)
opcion2 = tk.Radiobutton(ventana,text="Blue",variable=variable_control,value=2,command=cambiar_color)

opcion1.pack()
opcion2.pack()

ventana.mainloop()
