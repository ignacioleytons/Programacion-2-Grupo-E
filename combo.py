import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
#Crear ventana principal
ventana=tk.Tk()
ventana.title("Ejemplo COmbobox")
ventana.geometry("300x200")
#Etiqueta
etiqueta=tk.Label(ventana,text="Seleccione especialidad")
etiqueta.grid(row=0,column=0,padx=10,pady=10,sticky="w")
#crear combobox
opciones=["Cardiología","Neurología","Pediatría","Dermatología"]
combo=ttk.Combobox(ventana,values=opciones,state="readonly")
combo.current(0) #seleecionar primera opción pord defecto
combo.grid(row=0,column=1,padx=10,pady=10)
#Función para mostrar la selección
def mostrar():
    seleccion=combo.get()
    tk.messagebox.showinfo("Selección",f"Haz elegido:{seleccion}")
#Boton para confirmar seleccion
boton=tk.Button(ventana,text="Aceptar",command=mostrar)
boton.grid(row=1,columnspan=2,pady=15)
ventana.mainloop()