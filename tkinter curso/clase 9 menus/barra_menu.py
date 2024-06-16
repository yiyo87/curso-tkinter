import tkinter as tk

ventana = tk.Tk()#se importa le libreria tk

barra_menu = tk.Menu(ventana)#se crea un elemento con el objeto menu dentro de la ventana
ventana.config(menu=barra_menu)#se configura la ventana con el elemento creado anteriormente 

archivo_menu = tk.Menu(barra_menu)#dentro de la ventana se crea un menu 
barra_menu.add_cascade(label="Archivo",menu=archivo_menu)#y se agrega con el add cascade un me

archivo_menu.add_command(label="Nuevo")#dentro de archivo menun se fueron agregando el resto de elementos 
archivo_menu.add_command(label="Abrir")
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir")


ventana.mainloop()