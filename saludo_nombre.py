import tkinter

ventan = tkinter.Tk()

variable_nombre= tkinter.StringVar()

def cambiar_nombre():
    hola_nombre.configure(text="Hola " + variable_nombre.get())

hola_nombre = tkinter.Label(ventan, text="Hola Nombre", font=("Arial", 18), padx=20, pady=15)
hola_nombre.pack()

nombre = tkinter.Entry(ventan, font=("Arial", 16), textvariable= variable_nombre)
nombre.pack(padx=20, pady=15)

boton_cambio = tkinter.Button(ventan, text="Cambiar", font=("Arial", 16), command=cambiar_nombre)
boton_cambio.pack(padx=20, pady=15)



ventan.mainloop()