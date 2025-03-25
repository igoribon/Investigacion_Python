import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera ventana con Tkinter")

# Crear una etiqueta (widget)
etiqueta = tk.Label(ventana, text="¡Hola, Tkinter!")
etiqueta.pack()  # Ubicar la etiqueta en la ventana

# Crear un botón (widget)
def saludar():
    nueva_etiqueta = tk.Label(ventana, text="¡Hola, usuario!")
    nueva_etiqueta.pack()  # Se añade debajo de los widgets ya existentes


boton = tk.Button(ventana, text="Haz clic aquí", command=saludar)
boton.pack()

# Iniciar el loop de la ventana
ventana.mainloop()