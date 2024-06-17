import tkinter as tk

ventana = tk.Tk()#se crea la ventana 

canvas = tk.Canvas(ventana,width=500,height=300,bg="lightblue")#se cre dentro de ventan un rectangulo con algunas propiedades de estilo

rectangulo = canvas.create_rectangle(50,50,150,100, fill="green",outline="black",width=2,tags="rectangulo")# dentro de ese triangulo de crea otro rectangulo tambien con propiedades de estilo 
canvas.create_oval(200,50,300,150, fill="blue",outline="black",width=5)#se crea un ovalo dentro de la ventana 
canvas.create_polygon(350,50,400,100,400,150,350,150, fill="purple",outline="black",width=2)#se crea un poligono
canvas.create_line(100,200,100,200, fill="orange",width=5,dash=(5,2),capstyle="round")#se crea una linea dentro de la ventana 


canvas.pack()

ventana.mainloop()
