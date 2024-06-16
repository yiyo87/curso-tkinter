import tkinter as tk

ventana = tk.Tk()#se crea la ventana en donde se va a trabajar

menubutton = tk.Menubutton(ventana,text = "archivo")#importando la libreria tkinter se agrega un botin que despliega un menu 
menubutton.pack()

menu = tk.Menu(menubutton)
menubutton.config(menu=menu)

def abrir_archivo():#lo que hace esta funcion es que cada vez que se abre el menu y se elige abrir
    print("archivo abierto")# dentro de la consola sale el mensaje archivo abierto

menu.add_command(label="abrir",command=abrir_archivo)#aqui se agregan las funciones del menu tanto guardar como abrir 
menu.add_command(label="guardar")

ventana.mainloop()

