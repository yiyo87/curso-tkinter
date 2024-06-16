import tkinter as tk

ventana = tk.Tk()

ventana.title("mi ventana")
ventana.geometry("400x400")#se puede establecer como tamaño predeterminado  
ventana.minsize(400,200) #tamaño minimo al que se deja
ventana.maxsize(800,600)#solo llega hasta ese tamaño
ventana.iconbitmap("hogar.png")
ventana.configure(bg="lightblue")
ventana.resizable(False,False)#se bloauea el tamaño de la ventana 


ventana.mainloop()

