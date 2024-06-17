import tkinter as tk
from tkcalendar import DateEntry

ventana = tk.Tk()

date_entry = DateEntry(ventana,selectmode="day",locale="es_ES",year=2024,month=6,day=17,date_pattern="dd-mm-y")
date_entry.pack()

ventana.mainloop()

