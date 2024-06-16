import tkinter as tk

def on_click(event):# se crea la funcion que hace simplemente mostrar un mensaje
    print("boton presionado")

ventana = tk.Tk()#dentro de la varible ventana se llamand tanto al modulo como la funcion tk

button =tk.Button(ventana, text="haz click aqui")
button.pack()#dentro de la ventana se crea un boton el el mensaje haz click aqui

button.bind("<Button-1>", on_click)#solamente se genera la accion del mensaje con el click principal del mouse
#a este boton se le pasa un metodo que seria bind lo que hace bind es que cada vez que se aprieta un boton especificado se genera una accion

def on_key_press(event):
    if event.char == "a":
        print("tecla 'a' presionada")

ventana.bind("<KeyPress>", on_key_press)

def on_mouse_move(event):
    print(f"raton movido a {event.x},{event.y}")

ventana.bind ("<Motion>", on_mouse_move)
#esta funcion muestra por mensaje dentro de la consola las coordenadas en donde se encuentra el mouse
#solo se aplica dentro de la ventana


def on_click_text(event):
    print(f"Boton {event.widget['text']} presiondado")

ventana = tk.Tk()

buttons = [tk.Button(ventana,text=f"Boton {i}") for i in range(5)]

for button in buttons:
    button.pack()
    button.bind()
    button.bind("<Button-1>", on_click_text)
#lo que hace esta funcion es que crea una ventana con 3 botones que cada vez que se presiona con el boton izquierdo del mouse sale un mensaje de boton presionado


ventana.mainloop()
#lo que hace esta funcion es que cada vez que presiono el boton creado aparece un mensaje por consola 