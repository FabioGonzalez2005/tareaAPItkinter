import tkinter as tk
from tkinter import ttk

indice_actual = 0

def actualizar_producto(titulo_label, lista_productos):
    titulo_label.config(text=lista_productos.products[indice_actual].title)

def siguiente(titulo_label, lista_productos):
    global indice_actual
    if indice_actual < len(lista_productos.products) - 1:
        indice_actual += 1
        actualizar_producto(titulo_label, lista_productos)

def anterior(titulo_label, lista_productos):
    global indice_actual
    if indice_actual > 0:
        indice_actual -= 1
        actualizar_producto(titulo_label, lista_productos)

def mostrarProductos(lista_productos):
    ventanaProductos = tk.Tk()
    ventanaProductos.title("Productos de Fabio")
    ventanaProductos.geometry("400x400")

    canvas = tk.Canvas(ventanaProductos, width=400, height=400, background='#E4CCFF')
    canvas.pack()

    frame = tk.Frame(canvas)
    canvas.create_window(200, 100, window=frame)

    titulo = ttk.Label(frame, text=lista_productos.products[indice_actual].title, font=("Arial", 18), background='#E4CCFF')
    titulo.pack()

    boton_anterior = ttk.Button(frame, text="Anterior", command=lambda: anterior(titulo, lista_productos))
    boton_anterior.pack()

    boton_siguiente = ttk.Button(frame, text="Siguiente", command=lambda: siguiente(titulo, lista_productos))
    boton_siguiente.pack()

    ventanaProductos.mainloop()



    # r = request.get(URL, stream=True)
    # img = Image.open(r.raw)
    # imgttk = Imagettk(img)
    # label (imgttk)