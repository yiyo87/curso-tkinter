from tkinter import *

ventana = Tk()
ventana.title("ventana principal")
ventana.geometry("600x400")


def abrir_ventana_toplevel():
    ventana_toplevel = Toplevel(ventana)
    ventana_toplevel.title("ventana toplevel")
    ventana_toplevel.geometry("300x200+50+50")
    label = label(ventana_toplevel,text="ventanatoplevel")
    label.pack()

boton = Button(ventana,text="abrir ventana toplevel",command=abrir_ventana_toplevel)
boton.pack()

def cerrar_ventana_toplevel():
    ventana.destroy()

ventana.mainloop()