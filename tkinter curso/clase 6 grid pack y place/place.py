import tkinter as tk

ventana = tk.Tk()
ventana.title("ejemplo place")

ventana.geometry("300x300")

label1 = tk.Label(ventana, text="label 1")
label1.place(relx=0.25,rely=0.25)

label2 = tk.Label(ventana, text="label 2")
label2.place(relx=0.75,rely=0.75)

ventana.mainloop()