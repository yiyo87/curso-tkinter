import tkinter as tk #se importa la libreria

ventana = tk.Tk()#se crea una ventana

texto = tk.Text(ventana)#tambien se crea un cuadro de texto para poder escribir y que la barra de desplazamiento se pueda ocupar 

scrollbar_vertical = tk.Scrollbar(ventana)#se crea un variable con le funcion scrollbar dentro de la ventana
scrollbar_vertical.pack(side="right",fill="y")#y que se posicione dentro de la ventana a la derecha y que ocupe todo el eje y

scrollbar_vertical.config(command=texto.yview)#lo que hace el yview es principalmente que la barra de desplazamiento se mueva junto con el texto 
texto.config(yscrollcommand=scrollbar_vertical.set)
texto.pack(side="left",fill="both",expand=True)


ventana.mainloop()