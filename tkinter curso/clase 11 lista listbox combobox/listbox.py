import tkinter as tk#se importa la libreria

ventana = tk.Tk()#se crea la ventana
ventana.title("ejemplo de listbox")#se coloca el titutlo a la ventana

listbox = tk.Listbox(ventana,width=30, height=10,font=("Arial",12),fg="white",bg="black")#a esa lista de elementos se le da unas propiedades

listbox.insert(tk.END,"Elemento 1")#el tk.end es para posicionar los elementos al final 
listbox.insert(tk.END,"Elemento 2")
listbox.insert(tk.END,"Elemento 3")
listbox.insert(0,"Elemento 4")#lo numeros del princicio es para posicionar dentro de la ventana los elementos 
listbox.insert(2,"Elemento 5")

listbox.delete(2)#se elimina el elemento 2
listbox.delete(0)# se elimina el elemento 0 de la lista

"""
def on_seleccionar (event):#esta funcion hace que al tener elementos dentro de la ventana esta al hace clcik en una de ellas por consola muestre cual es el indice en el que se encuentran
    indice = listbox.curselection()
    elemento = listbox.get(indice)
    print(f"seleccionado:{elemento}")

listbox.bind("<<ListboxSelect>>",on_seleccionar)#aqui se llama la funcion 
"""

def on_clic(event):
    print("click en el listbox")

def on_doble_clic(event):
    print("doble clic en el listbox")

listbox.bind("<Button-1>",on_clic)
listbox.bind("<Double-Button-1>",on_doble_clic)


listbox.pack()
ventana.mainloop()
