import tkinter as tk

ventana= tk.Tk()#se crea la ventana

canvas = tk.Canvas(ventana,width=500,height=300,bg="lightblue")#se da propiedades del estilo a la ventana
canvas.pack(fill="both",expand=True)#esto hace que la ventana junto con las propiedades se expanda dentro de la ventana

canvas.create_text(150,50,text="aprendiendo canvas",fill= "darkgreen",font=("courier",12,"italic"),justify="center")
#aqui se coloca un texto con algunas propiedades de estilo para que resalte 
canvas.pack()

ventana.mainloop()#se mantiene la ventana abierta 