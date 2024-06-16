import tkinter as tk

ventana = tk.Tk()# se crea una ventana 


barra_menu = tk.Menu(ventana)#se crea una ventana con el menu 
ventana.config(menu=barra_menu)# aqui se configura que habra una barra de menu dentro de la ventana 

archivo_menu = tk.Menu(barra_menu)
barra_menu.add_cascade(label="archivo",menu=archivo_menu)


#se agregan los menu dentro de la ventana 
# en este caso se agerga dentro de el menu archivo se crea nuevo y abrir
archivo_menu.add_command(label="Nuevo")
archivo_menu.add_command(label="Abrir")

archivo_menu.add_separator()

archivo_menu.add_command(label="Salir")

#añadir un menu "editar" a la barra de menu
#luego se crea un menu que seria editar y dentro de editar estaria los elementos copiar y cortar
editar_menu = tk.Menu(barra_menu)
barra_menu.add_cascade(label="editar",menu=editar_menu)

editar_menu.add_command(label="Copiar")
editar_menu.add_command(label="Cortar")

ventana.mainloop()#se mantiene siempre abierta la ventana 