import tkinter as tk #se hace la importancion de la libreria

ventana = tk.Tk()#crea la ventana

def mostrar_menu_contextual(event):#se crea la funcion en donde si se hace click derecho con el mouse aparece un menu 
    menu_contextual.tk_popup(event.x_root,event.y_root)

menu_contextual = tk.Menu(ventana,tearoff=0)
menu_contextual.add_command(label="Cortar")
menu_contextual.add_command(label="Copiar")
menu_contextual.add_command(label="Pegar")

ventana.bind("<Button-3>",mostrar_menu_contextual)#se crea el evento que con el click derecho se despliega un menu con las opciones descritas mas arriba 

ventana.mainloop()
