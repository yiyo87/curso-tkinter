#FRAMES
#los frames es como los cuadros dentro de los cuadros vealo como si fuera html
import tkinter as tk
#se importa la libreria de trabajo
ventana= tk.Tk()
#se crea una nueva ventana 
ventana.title ("Mi ventana")
#se le da el titulo a la ventana
ventana.geometry("600x400")
ventana.config(bg="lightblue")
#se da las dimensiones a la nueva ventana 


###FRAMES###
"""
#se crean los frame que vendrian siendo como cuadros dentro de cuadros dentro de la ventana 
frame1 = tk.Frame(ventana)
frame1.configure(bg="red", width=300,height=200,bd=5)
frame1.pack()#aqui se invocan las ventanas tanto de los frames como de la ventana principal que se crea dentro de un loops para que no se cierre 

frame2 = tk.Frame(frame1)
frame2.configure (width=100,height=100,bg="blue",bd=5)
frame2.pack()#aqui se invocan las ventanas tanto de los frames como de la ventana principal que se crea dentro de un loops para que no se cierre 

boton = tk.Button(frame1,text="hola mundo")
boton.pack()
"""
###LABELFRAME###
labelframe = tk.LabelFrame(ventana,text="grupo de widgets",bg="yellow",padx=10,pady=10)
labelframe.configure(width=300,height=200)
labelframe.pack()

ventana.mainloop()
