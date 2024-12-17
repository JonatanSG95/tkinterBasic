import tkinter

ventana = tkinter.Tk()

#ventana.config(bg="#0b4ef4")

titulo = tkinter.Label(ventana, text="Hola mundo", font=("Arial", 16, "bold"), padx=20, pady=20, bg="#0b4ef4", fg="#f79014")

titulo.pack()

ventana.mainloop()