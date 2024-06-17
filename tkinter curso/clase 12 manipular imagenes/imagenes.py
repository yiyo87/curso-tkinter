import tkinter as tk

ventana = tk.Tk()

imagen = tk.PhotoImage(file="budgie-logo.png")

etiqueta = tk.label(ventana,image=imagen)

etiqueta.pack()
boton.pack()

ventana.mainloop()