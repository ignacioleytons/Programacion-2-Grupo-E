#importar librerias
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime 

# Funciones Medicamentos
# Función para enmascarar fecha
def enmascarar_fecha(texto):
    limpio="".join(filter(str.isdigit,texto))
    formato_final=""
    if len(limpio)>8:
        limpio=limpio[:8]
    if len(limpio)>4:
            formato_final=f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
    elif len(limpio)>2:
            formato_final = f"{limpio[:2]}-{limpio[2:]}"
    else:
            formato_final = limpio
            
    if fechaM.get() != formato_final:
        fechaM.delete(0, tk.END)
        fechaM.insert(0, formato_final)    
    return True

#guardar medicamentos en archivo
def guardar_medicamentos_en_archivo():
    with open("medicamento.txt", "w", encoding="utf-8") as archivo:
        for medicamento in medicamento_data:
            archivo.write(f"{medicamento['Nombre']}|{medicamento['Presentacion']}|{medicamento['Dosis']}|{medicamento['Fecha Vencimiento']}\n")

#cargar medicamentos desde archivo
def cargar_desde_archivo_medicamentos():
    try:
        with open("medicamento.txt", "r", encoding="utf-8") as archivo:
            medicamento_data.clear()
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 4:
                    medicamento = {
                        "Nombre": datos[0],
                        "Presentacion": datos[1],
                        "Dosis": datos[2],
                        "Fecha Vencimiento": datos[3]
                    }
                    medicamento_data.append(medicamento)
        cargar_treeview_medicamentos()
    except FileNotFoundError:
        open("medicamento.txt", "w", encoding="utf-8").close()

#funcion registrar medicamento
def registrarMedicamento():
    medicamento = {
        "Nombre": nombreM.get(),
        "Presentacion": presentacion_var.get(),
        "Dosis": dosisM.get(),
        "Fecha Vencimiento": fechaM.get()
    }
    if medicamento["Nombre"] == "" or medicamento["Presentacion"] == "" or medicamento["Dosis"] == "" or medicamento["Fecha Vencimiento"] == "":
        messagebox.showwarning("Registro", "Todos los campos son obligatorios")
        return
    medicamento_data.append(medicamento)
    guardar_medicamentos_en_archivo()
    cargar_treeview_medicamentos()

#funcion eliminar medicamento
def eliminarMedicamento():
    seleccionado = treeviewM.selection()
    if seleccionado:
        indice = int(seleccionado[0])      
        id_item = seleccionado[0]
        if messagebox.askyesno("Eliminar Medicamento", f"¿Estás seguro de eliminar el medicamento {treeviewM.item(id_item, 'values')[0]}?"):
            del medicamento_data[indice]
            guardar_medicamentos_en_archivo()
            cargar_treeview_medicamentos()
            messagebox.showinfo("Eliminar Medicamento", "Medicamento eliminado exitosamente")
    else: 
        messagebox.showwarning("Eliminar Medicamento", "No se ha seleccionado ningún medicamento.")

#lista de medicamentos
medicamento_data = []

#cargar treeview
def cargar_treeview_medicamentos():
    for med in treeviewM.get_children():
        treeviewM.delete(med)
    for i, item in enumerate(medicamento_data):
        treeviewM.insert(
            "", "end", iid=str(i),
            values=(item["Nombre"], item["Presentacion"], item["Dosis"], item["Fecha Vencimiento"])
        )

# VENTANA PRINCIPAL
ventana = tk.Tk()
ventana.title("Gestión de Medicamentos")
ventana.geometry("800x600")

# Formulario Medicamentos
label_nombreM = tk.Label(ventana, text="Nombre del Medicamento:")
label_nombreM.grid(row=0, column=0, sticky="w", pady=5, padx=5)
nombreM = tk.Entry(ventana)
nombreM.grid(row=0, column=1, sticky="w", pady=5, padx=5)

label_presentacionM = tk.Label(ventana, text="Presentación:")
label_presentacionM.grid(row=1, column=0, sticky="w", pady=5, padx=5)
presentacion_var = tk.StringVar()
comboPresentacion = ttk.Combobox(ventana, textvariable=presentacion_var, values=["Tabletas", "Jarabe", "Inyectable", "Cápsulas", "Otro"])
comboPresentacion.grid(row=1, column=1, sticky="w", pady=5, padx=5)

label_dosisM = tk.Label(ventana, text="Dosis:")
label_dosisM.grid(row=2, column=0, sticky="w", pady=5, padx=5)
dosisM = tk.Entry(ventana)
dosisM.grid(row=2, column=1, sticky="w", pady=5, padx=5)

label_fechaM = tk.Label(ventana, text="Fecha de Vencimiento:")
label_fechaM.grid(row=3, column=0, sticky="w", pady=5, padx=5)
validacion_fecha = ventana.register(enmascarar_fecha)
fechaM = ttk.Entry(ventana, validate="key", validatecommand=(validacion_fecha, "%P"))
fechaM.grid(row=3, column=1, sticky="w", pady=5, padx=5)

# Botones
btn_frameM = tk.Frame(ventana)
btn_frameM.grid(row=4, column=0, columnspan=2, pady=10, sticky="w")

btn_registrarM = tk.Button(btn_frameM, text="Registrar", bg="green", fg="white", command=registrarMedicamento)
btn_registrarM.grid(row=0, column=0, padx=5)
btn_eliminarM = tk.Button(btn_frameM, text="Eliminar", bg="red", fg="white", command=eliminarMedicamento)
btn_eliminarM.grid(row=0, column=1, padx=5)

# Treeview Medicamentos
treeviewM = ttk.Treeview(ventana, columns=("Nombre", "Presentacion", "Dosis", "Fecha"), show="headings")
treeviewM.heading("Nombre", text="Nombre")
treeviewM.heading("Presentacion", text="Presentación")
treeviewM.heading("Dosis", text="Dosis")
treeviewM.heading("Fecha", text="Fecha Vencimiento")
treeviewM.column("Nombre", width=150)
treeviewM.column("Presentacion", width=120, anchor="center")
treeviewM.column("Dosis", width=80, anchor="center")
treeviewM.column("Fecha", width=120, anchor="center")
treeviewM.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)
scroll_yM = ttk.Scrollbar(ventana, orient="vertical", command=treeviewM.yview)
treeviewM.configure(yscrollcommand=scroll_yM.set)
scroll_yM.grid(row=5, column=2, sticky="ns")

# cargar datos guardados
cargar_desde_archivo_medicamentos()

ventana.mainloop()
