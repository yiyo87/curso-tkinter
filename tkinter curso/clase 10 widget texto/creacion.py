import tkinter as tk
from tkinter.scrolledtext import ScrolledText # se hace la importacion para que se cree un scroll dentro de la ventana

ventana = tk.Tk()#se crea la ventana 
texto = tk.Text(ventana, width=40,height=10, wrap="word",bg="lightgray",fg="black",padx=100,pady=100,font=("helvetica",12)) # se hace que dentro de la ventana se pueda escribir un texto

texto.insert("1.0","Bienvenido a nuestro editor de texto")#se inserta el texto dentro de la ventana
texto.insert("end","\n\neste es un eje,plo de texto resaltado","resaltado")
texto.tag_configure("resaltado",background="yellow",foreground="black")
contenido = texto.get("1.0","end")
print (contenido)
texto.pack()

texto_desplazable = ScrolledText(ventana) # dentro de ventana se crea una variable que se llama texto_desplegable en donde se crea el scrolledtext
texto_desplazable.pack()

ventana.mainloop()