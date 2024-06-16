import tkinter as tk

ventana = tk.Tk()
ventana.title("ejemplo practico de pack")

frame_botones = tk.Frame(ventana,bg="blue")#esto quiere decir que dentro de una ventana se crea un contenedor para luego albergar los botones 
frame_botones.pack(padx=10)

boton1 = tk.Button(frame_botones,text="Boton 1")
boton1.pack(side="left",padx=5)

boton2 = tk.Button(frame_botones,text="Boton 2")
boton2.pack(side="left",padx=5)

boton3 = tk.Button(frame_botones,text="Boton 3")
boton3.pack(side="left",padx=5)

ventana.mainloop()
# esto hace que muestre por pantalla un boton al lado del otro por default los elementos se agrupan de arriba hacia abajo 