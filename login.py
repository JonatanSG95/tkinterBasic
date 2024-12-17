import tkinter

ventana = tkinter.Tk()

#funcion
def login():
    nombre = var_nombre.get()
    password = var_password.get()

    if nombre == "jonatan" and password == "admin123":
        mensaje_label.configure(text="Ingreso correcto")
    else:
        mensaje_label.configure(text="Usuario o Password incorrecto")

#variables
var_nombre = tkinter.StringVar()
var_password = tkinter.StringVar()


nombre_label = tkinter.Label(ventana, text="Nombre de Usuario", font=("Arial", 18))
nombre_entry = tkinter.Entry(ventana, font=("Arial", 16), textvariable=var_nombre)
password_label = tkinter.Label(ventana, text="Password", font=("Arial", 18))
password_entry = tkinter.Entry(ventana, font=("Arial", 16), textvariable=var_password)
boton_ingreso = tkinter.Button(ventana, text="Ingresar", font=("Arial", 18), command=login)

nombre_label.pack(padx=20, pady=15)
nombre_entry.pack(padx=20, pady=15)
password_label.pack(padx=20, pady=15)
password_entry.pack(padx=20, pady=15)
boton_ingreso.pack(padx=20, pady=15)

mensaje_label = tkinter.Label(ventana, text="", font=("Arial", 18))
mensaje_label.pack(padx=20, pady=15)

ventana.mainloop()