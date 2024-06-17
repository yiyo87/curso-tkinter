import tkinter as tk
from tkcalendar import Calendar

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Calendar")

# Crear y empacar el calendario
cal = Calendar(ventana, selectmode='day', date_pattern='yyyy-mm-dd')
cal.pack(pady=20)

# Definir la función que imprimirá la fecha seleccionada
def print_date(date):
    print(date)

# Vincular la selección del calendario al evento
cal.bind("<<CalendarSelected>>", lambda event: print_date(cal.get_date()))

# Iniciar el bucle principal de la interfaz
ventana.mainloop()