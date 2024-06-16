import tkinter as tk

ventana = tk.Tk()#crea la ventana

decimal = tk.DoubleVar(value=3.14)#se crea una variable con el valor de 3.14

control_dslizante = tk.Scale(ventana, variable = decimal,from_=0,to=10,resolution=0.01,orient=tk.HORIZONTAL)
#esto es una barra que comienza desde 0 hasta 10 .scale es importante para poder utilizar el control 
control_dslizante.pack()

ventana.mainloop()#con esto la ventana se mantiene siempre abierto