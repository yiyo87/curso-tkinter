import tkinter as tk

from tkinter import filedialog

def abrir_archivo():
    file_path = filedialog.askopenfilename(filetypes=[("archivos de texto","*.txt"),("todos los achivos","*.*")])
    if file_path:
        with open(file_path,"r")as file_obj:
            contenido = file_obj.read()
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.INSERT,contenido)


def guardar_archivo():
        file_path = filedialog.askopenfilename(filetypes=[("archivos de texto","*.txt"),("todos los achivos","*.*")])
        if file_path:
             with open(file_path,"w")as file_obj:
                contenido = text_widget.get(1.0, tk.END)
                file_obj.write(contenido)

ventana = tk.Tk()
ventana.title ("editor de archivos des texto")

text_widget = tk.Text(ventana,wrap="word")
text_widget.pack(expand=True,fill="both")

abrir_button = tk.Button(ventana,text="abrir archivo",command=abrir_archivo)
abrir_button.pack(side="left")

guardar_button = tk.Button(ventana,text="guardar archivo",command=guardar_archivo)
guardar_button.pack(side="right")

ventana.mainloop()