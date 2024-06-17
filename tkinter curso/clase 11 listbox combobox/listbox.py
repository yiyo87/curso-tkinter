import tkinter as tk

ventana = tk.Tk()#se crea ventana
ventana.title("ejemplo de listbox")#se le da titutlo a la ventana

listbox = tk.Listbox(ventana,width=30,height=10,font=("Arial",12),fg="white",bg="black")#se entrega propiedades a la ventana 
listbox.insert(tk.END,"elemento 1")#se insertan elementos a la ventana
listbox.insert(tk.END,"elemento 2")
listbox.insert(tk.END,"elemento 3")
listbox.insert(0,"elemento 4")
listbox.insert(2,"elemento 5")

listbox.delete(2)# se eliminan estos elementos de la ventana 
listbox.delete(0)
"""
def on_seleccionar(event):#se crea esta funcion que lo que hace es que dentro de la ventana los elementos tienen la propiedad de que si se hace click al elemento por consola sale que elemento estas pinchando 
    indice = listbox.curselection()
    elemento = listbox.get(indice)
    print(f"seleccionado:{elemento}")

listbox.bind("<<ListboxSelect>>",on_seleccionar)#con le bind se vincula un evento especifico dentro de una funcion 
"""
def on_click(event):
    print("clic en el listbox")

def on_doble_clic(event):
    print("doble clic en el listbox")

listbox.bind("<Button-3>",on_click)
listbox.bind("<Double-Button-1>",on_doble_clic)



listbox.pack()
ventana.mainloop()#se mantiene la ventana abierta 