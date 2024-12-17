import tkinter

print(bin(ord("h"))[2:])

ventan = tkinter.Tk()

def convertir():
    text = cuadro_texto.get("1.0", tkinter.END)
    textoBinario = ""

    for letra in text:
        if letra == " ":
            textoBinario += " "
        textoBinario += bin(ord(letra))[2:]

    cuadro_texto.delete("1.0",tkinter.END)
    cuadro_texto.insert("1.0", textoBinario)



label_texto = tkinter.Label(ventan, text="Ingrese su texto", font=("Arial",18))
cuadro_texto = tkinter.Text(ventan, width=60, height=20)
boton_cambio = tkinter.Button(ventan, text="A binario", font=("Arial", 16), command=convertir)
label_texto.pack(padx=20, pady=15)
cuadro_texto.pack(padx=20, pady=15)
boton_cambio.pack(padx=20, pady=15)

ventan.mainloop()