import tkinter as tk

ventana = tk.Tk()#se crea la ventana

imagen = tk.PhotoImage(file="budgie-logo.png")#se inserta dentro de la ventana la imagen que en este caso no me resulto

etiqueta = tk.label(ventana,image=imagen)#se agrega un label a la ventana

etiqueta.pack()

ventana.mainloop()#para que la ventana no se cierre 