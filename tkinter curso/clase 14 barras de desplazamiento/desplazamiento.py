import tkinter as tk #se importa la libreria

ventana = tk.Tk()#se crea una ventana

scrollbar_vertical = tk.Scrollbar(ventana)#se crea un variable con le funcion scrollbar dentro de la ventana
scrollbar_vertical.pack(side="right",fill="y")#y que se posicione dentro de la ventana a la derecha y que ocupe todo el eje y

ventana.mainloop()