from tkinter import Tk,Label,Button, filedialog
from PIL import Image,ImageTk
from PIL import ImageFilter

ventana = Tk()
etiqueta = Label (ventana)

imagen_pil = Image.open("budgie-logo.png")
imagen_tk = ImageTk.PhotoImage(imagen_pil)

boton = Button(ventana,image=imagen_tk)
boton.pack()

ventana.mainloop()