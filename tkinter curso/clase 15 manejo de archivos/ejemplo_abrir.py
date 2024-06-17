import  tkinter as tk

from tkinter import filedialog# esta import es para pode abrir archivo

def abrir_archivo():
    file_path = filedialog.askopenfilename(filetypes=[("archivos de texto","*txt"),("todos los archivos","*.*")])
    if file_path:#esto abre cualquier tipo de archivo
        with open(file_path,"r") as file_obj:
            contenido = file_obj.read()
            text_widget.delete(1.0,tk.END)
            text_widget.insert(tk.INSERT,contenido)

ventana = tk.Tk()
ventana.title("visor de archivos de texto")

text_widget = tk.Text(ventana,wrap="word")#cuadro de texto

text_widget.pack(expand=True,fill="both")# se expande 

boton_abrir = tk.Button(ventana,text="Abrir",command=abrir_archivo)

boton_abrir.pack()

ventana.mainloop()