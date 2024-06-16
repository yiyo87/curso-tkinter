#lo que tiene el checkbutton es que se puede elegir varias opciones a la vez 
#como a diferencia de de radiobutton que es solamente para elegir 1 opcion 

import tkinter as tk

ventana = tk.Tk()

ventana.title("ejemplo radiobutton")

variable_check1 = tk.BooleanVar()

def on_checkbutton_cambio():
    if variable_check1.get():
        boton.config(state="normal")
    else:
        boton.config(state="disabled")

check1 = tk.Checkbutton(ventana,text="Habilitar Boton",variable=variable_check1,command=on_checkbutton_cambio)
boton = tk.Button(ventana,text="Boton",state="disabled")

check1.pack()
boton.pack()
#lo que hace esta funcion es que si no esta seleccionada el checkbox no se puede dar click al boton que esta abajo de la opcion 

ventana.mainloop()