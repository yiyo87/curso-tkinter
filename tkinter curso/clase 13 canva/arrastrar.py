import tkinter as tk

def iniciar_arrastre(event):#estas funciones trabajan con las coordenadas tanto x como y
    global objeto_seleccionado
    objeto_seleccionado = canvas.find_closest(event.x,event.y)

def terminar_arrastre (event):#ya con esta funcion es que termina el ciclo de arrastrar
    global objeto_seleccionado
    if objeto_seleccionado:
        x,y= event.x,event.y
        canvas.move(objeto_seleccionado,x - canvas.coords(objeto_seleccionado)[0],y - canvas.coords(objeto_seleccionado)[1])
        objeto_seleccionado = None

ventana = tk.Tk()
canvas = tk.Canvas(ventana,width=500,height=300)#hace que dentro de la ventana un canvas que luego se va a ocupar para poder moverlo de un ligar a otro 
canvas.pack()

objeto_seleccionado = None

rectangulo = canvas.create_rectangle(100,100,200,200,fill="blue",tags="rectangulo")

canvas.tag_bind("rectangulo","<ButtonPress-1>",iniciar_arrastre)# significa que cuando tomas el resctangulo con el mouse el momento de terminar de arrastrar se termina la funcion
canvas.tag_bind("rectangulo","<ButtonRelease-1>",terminar_arrastre)

ventana.mainloop()