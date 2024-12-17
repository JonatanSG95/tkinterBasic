import tkinter

ventana = tkinter.Tk()

lista_tareas = ["Cocinar", "Limpiar", "Lavar Ropa", "Ordenar pieza", "Conseguir laburo"]

for tarea in lista_tareas:
    tkinter.Checkbutton(ventana, text=tarea, font=("Arial", 16)).pack(padx=20,pady=15)


ventana.mainloop()