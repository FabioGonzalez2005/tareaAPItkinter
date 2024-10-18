import tkinter as tk
from tkinter import ttk

indice_actual = 0

def actualizar_producto(titulo_label, lista_productos):
    titulo_label.config(text=lista_productos.products[indice_actual].title)

def siguiente(titulo_label, descripcion_label, categoria_label, precio_label, rating_label, stock_label, tags_label, marca_label, sku_label, lista_productos):
    global indice_actual
    if indice_actual < len(lista_productos.products) - 1:
        indice_actual += 1
        actualizar_producto(titulo_label, descripcion_label, categoria_label, precio_label, rating_label, stock_label, tags_label, marca_label, sku_label)

def anterior(titulo_label, descripcion_label, categoria_label, precio_label, rating_label, stock_label, tags_label, marca_label, sku_label):
    global indice_actual
    if indice_actual > 0:
        indice_actual -= 1
        actualizar_producto(titulo_label, descripcion_label, categoria_label, precio_label, rating_label, stock_label, tags_label, marca_label, sku_label)


def mostrarProductos(lista_productos):
    ventanaProductos = tk.Tk()
    ventanaProductos.title("Productos de Fabio")
    ventanaProductos.geometry("500x600")

    canvas = tk.Canvas(ventanaProductos, width=500, height=600, background='#E4CCFF')
    canvas.pack()

    frame = tk.Frame(canvas)
    canvas.create_window(250, 200, window=frame)

    titulo = ttk.Label(frame, text="", font=("Arial", 16), background='#E4CCFF')
    titulo.pack()

    descripcion = ttk.Label(frame, text="", font=("Arial", 12), background='#E4CCFF')
    descripcion.pack()

    categoria = ttk.Label(frame, text="", font=("Arial", 12), background='#E4CCFF')
    categoria.pack()

    precio = ttk.Label(frame, text="", font=("Arial", 12), background='#E4CCFF')
    precio.pack()

    rating = ttk.Label(frame, text="", font=("Arial", 12), background='#E4CCFF')
    rating.pack()

    stock = ttk.Label(frame, text="", font=("Arial", 12), background='#E4CCFF')
    stock.pack()

    tags = ttk.Label(frame, text="", font=("Arial", 12), background='#E4CCFF')
    tags.pack()

    marca = ttk.Label(frame, text="", font=("Arial", 12), background='#E4CCFF')
    marca.pack()

    sku = ttk.Label(frame, text="", font=("Arial", 12), background='#E4CCFF')
    sku.pack()

    boton_anterior = ttk.Button(frame, text="Anterior", command=lambda: anterior(titulo, descripcion, categoria, precio, rating, stock, tags, marca, sku))
    boton_anterior.pack(side=tk.LEFT, padx=10, pady=20)

    boton_siguiente = ttk.Button(frame, text="Siguiente", command=lambda: siguiente(titulo, descripcion, categoria, precio, rating, stock, tags, marca, sku))
    boton_siguiente.pack(side=tk.RIGHT, padx=10, pady=20)

    actualizar_producto(titulo, descripcion, categoria, precio, rating, stock, tags, marca, sku)

    ventanaProductos.mainloop()



    # r = request.get(URL, stream=True)
    # img = Image.open(r.raw)
    # imgttk = Imagettk(img)
    # label (imgttk)