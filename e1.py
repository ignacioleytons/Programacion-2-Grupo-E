import tkinter as tk
from tkinter import messagebox
ventanaprincipal=tk.Tk()
ventanaprincipal.title("Sistema de registro de pacientes")
ventanaprincipal.geometry("600x400")
ventanaprincipal.configure(bg="lightblue")
def nuevopaciente():
    ventanaregistro=tk.Toplevel(ventanaprincipal)
    ventanaregistro.title("Registro de pacientes")
    ventanaregistro.geometry("400x400")
    ventanaregistro.configure(bg="lightblue")
    #nombre
    nombrelabel=tk.Label(ventanaregistro, text="Nombre: ", bg="lightblue")
    nombrelabel.grid(row=0, column=0, padx=10, pady=5, sticky="n")
    entrynombre=tk.Entry(ventanaregistro)
    entrynombre.grid(row=0, column=1, padx=10, pady=5, sticky="we")
    #direccion
    nombrelabel=tk.Label(ventanaregistro, text="Direccion: ", bg="lightblue")
    nombrelabel.grid(row=1, column=0, padx=10, pady=5, sticky="n")
    entrydireccion=tk.Entry(ventanaregistro)
    entrydireccion.grid(row=1, column=1, padx=10, pady=5, sticky="we")
    #telefono
    nombrelabel=tk.Label(ventanaregistro, text="Telefono: ", bg="lightblue")
    nombrelabel.grid(row=2, column=0, padx=10, pady=5, sticky="n")
    entrytelefono=tk.Entry(ventanaregistro)
    entrytelefono.grid(row=2, column=1, padx=10, pady=5, sticky="we")
     #sexo(radiobutton)
    sexolabel=tk.Label(ventanaregistro, text="Sexo: ",bg="lightblue")
    sexolabel.grid(row=3, column=0,padx=10,pady=5, sticky="n")
    sexo=tk.StringVar(value="Masculino")
    rbmasculino=tk.Radiobutton(ventanaregistro,text="Masculino",variable=sexo,value="Masculino",bg="lightblue")
    rbmasculino.grid(row=3,column=1,sticky="we")
    rbfemenino=tk.Radiobutton(ventanaregistro,text="Femenino",variable=sexo,value="Femenino",bg="lightblue")
    rbfemenino.grid(row=4,column=1,sticky="we")
    #enfermedades base(checkbutton)
    enflabel=tk.Label(ventanaregistro, text="Enfermedades base: ",bg="lightblue")
    enflabel.grid(row=5, column=0, padx=10, pady=5, sticky="w")
    diabetes=tk.BooleanVar()
    hipertension=tk.BooleanVar()
    asma=tk.BooleanVar()
    cbdiabetes=tk.Checkbutton(ventanaregistro,text="Diabetes",variable=diabetes,bg="lightblue")
    cbdiabetes.grid(row=5,column=1,sticky="w")
    cbhipertension=tk.Checkbutton(ventanaregistro,text="Hipertension",variable=hipertension,bg="lightblue")
    cbhipertension.grid(row=6,column=1,sticky="w")
    cbasma=tk.Checkbutton(ventanaregistro,text="Asma",variable=asma,bg="lightblue")
    cbasma.grid(row=7,column=1,sticky="w")
    def registrardatos():
        enfermedades=[]
        if diabetes.get():
            enfermedades.append("Diabetes")
        if hipertension.get():
            enfermedades.append("Hipertension")
        if asma.get():
            enfermedades.append()("Asma")
        if len(enfermedades)>0:
            enfermedadestexto=','.join(enfermedades)
        else:
            enfermedadestexto="Ninguna"
    #cadena para mostrar todos los datos del formulario
        info=(
            f"Nombre:{entrynombre.get()}\n"
            f"Direccion:{entrydireccion.get()}\n"
            f"telefono:{entrytelefono.get()}\n"
            f"sexo:{sexo.get()}\n"
            f"enfermedades:{enfermedadestexto}"
        )
        messagebox.showinfo("Datos Registrados", info)
        ventanaregistro.destroy() #cierra la ventana tras el mensaje
    btnregistrar=tk.Button(ventanaregistro,text="Datos Registrados",command=registrardatos)
    btnregistrar.grid(row=9,column=0,columnspan=2,pady=15)
def buscarpaciente():
    messagebox.showinfo("Buscar Paciente","Este es el espacio para eliminar un paciente")
def eliminarpaciente():
    messagebox.showinfo("Eliminar Paciente","Este es el espacio para eliminar un paciente")
def nuevodoctor():
    ventanaregistro=tk.Toplevel(ventanaprincipal)
    ventanaregistro.title("Registro de pacientes")
    ventanaregistro.geometry("400x400")
    ventanaregistro.configure(bg="lightblue")
    #nombre
    nombrelabel=tk.Label(ventanaregistro, text="Nombre: ", bg="lightblue")
    nombrelabel.grid(row=0, column=0, padx=10, pady=5, sticky="n")
    entrynombre=tk.Entry(ventanaregistro)
    entrynombre.grid(row=0, column=1, padx=10, pady=5, sticky="we")
    #direccion
    nombrelabel=tk.Label(ventanaregistro, text="Direccion: ", bg="lightblue")
    nombrelabel.grid(row=1, column=0, padx=10, pady=5, sticky="n")
    entrydireccion=tk.Entry(ventanaregistro)
    entrydireccion.grid(row=1, column=1, padx=10, pady=5, sticky="we")
    #telefono
    nombrelabel=tk.Label(ventanaregistro, text="Telefono: ", bg="lightblue")
    nombrelabel.grid(row=2, column=0, padx=10, pady=5, sticky="n")
    entrytelefono=tk.Entry(ventanaregistro)
    entrytelefono.grid(row=2, column=1, padx=10, pady=5, sticky="we")
     #sexo(radiobutton)
    sexolabel=tk.Label(ventanaregistro, text="Sexo: ",bg="lightblue")
    sexolabel.grid(row=3, column=0,padx=10,pady=5, sticky="n")
    sexo=tk.StringVar(value="Masculino")
    rbmasculino=tk.Radiobutton(ventanaregistro,text="Masculino",variable=sexo,value="Masculino",bg="lightblue")
    rbmasculino.grid(row=3,column=1,sticky="we")
    rbfemenino=tk.Radiobutton(ventanaregistro,text="Femenino",variable=sexo,value="Femenino",bg="lightblue")
    rbfemenino.grid(row=4,column=1,sticky="we")
def buscardoctor():
    messagebox.showinfo("Buscar doctor","Este es el espacio para buscar un doctor")
def eliminardoctor():
    messagebox.showinfo("Eliminar doctor","Este es el espacio para eliminar un doctor")
 
#barra de menu
barraMenu=tk.Menu(ventanaprincipal)
ventanaprincipal.config(menu=barraMenu)
#Menu paciente
menuPaciente=tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Pacientes",menu=menuPaciente)
menuPaciente.add_command(label="Nuevo Paciente",command=lambda:nuevopaciente())
menuPaciente.add_command(label="Buscar Paciente",command=lambda:buscarpaciente())
menuPaciente.add_command(label="Eliminar Paciente",command=lambda:eliminarpaciente())
menuPaciente.add_separator()
menuPaciente.add_command(label="Salir",command=ventanaprincipal.quit)
#menu ayuda
menuAyuda=tk.Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)
menuAyuda.add_command(label="Salir",command=ventanaprincipal.quit)
menuAyuda.add_command(label="acerca de", command=lambda:messagebox.showinfo("acerca de", "version 1.0-sistema Biomedicina"))
"menu doctores"
menuDoctores=tk.Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Doctores", menu=menuDoctores)
menuDoctores.add_command(label="Nuevo Doctor", command=lambda:nuevodoctor())
menuDoctores.add_command(label="Buscar Doctor", command=lambda:buscardoctor())
menuDoctores.add_command(label="Eliminar Doctor", command=lambda:eliminardoctor())
menuDoctores.add_command(label="Salir",command=ventanaprincipal.quit)
ventanaprincipal.mainloop()
 