import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests

indice_actual = 0

def actualizar_producto(titulo_label, descripcion_label, categoria_label, precio_label, rating_label, stock_label, tags_label, marca_label, sku_label, img_label, lista_productos):
    producto = lista_productos.products[indice_actual]

    titulo_label.config(text=producto.title)
    descripcion_label.config(text=producto.description)
    categoria_label.config(text=f"Categoria: {producto.category}")
    precio_label.config(text=f"{producto.price}€")
    rating_label.config(text=f"{producto.rating} ★")
    stock_label.config(text=f"Stock: {producto.stock}")
    tags_label.config(text=f"#{', #'.join(producto.tags)}")
    marca_label.config(text=producto.brand)
    sku_label.config(text=producto.sku)

    r = requests.get(producto.thumbnail, stream=True)
    img_data = r.raw
    img = Image.open(img_data)
    img_tk = ImageTk.PhotoImage(img)
    img_label.config(image=img_tk)
    img_label.image = img_tk

def siguiente(titulo_label, descripcion_label, categoria_label, precio_label, rating_label, stock_label, tags_label, marca_label, sku_label, img_label, lista_productos):
    global indice_actual
    if indice_actual < len(lista_productos.products) - 1:
        indice_actual += 1
        actualizar_producto(titulo_label, descripcion_label, categoria_label, precio_label, rating_label, stock_label, tags_label, marca_label, sku_label, img_label, lista_productos)

def anterior(titulo_label, descripcion_label, categoria_label, precio_label, rating_label, stock_label, tags_label, marca_label, sku_label, img_label, lista_productos):
    global indice_actual
    if indice_actual > 0:
        indice_actual -= 1
        actualizar_producto(titulo_label, descripcion_label, categoria_label, precio_label, rating_label, stock_label, tags_label, marca_label, sku_label, img_label, lista_productos)

def mostrarProductos(lista_productos):
    ventanaProductos = tk.Tk()
    ventanaProductos.title("Productos de Fabio")
    ventanaProductos.geometry("500x700")
    ventanaProductos.configure(background='#E4CCFF')

    frame = tk.Frame(ventanaProductos, background='#E4CCFF')
    frame.pack(pady=10, padx=10)

    img_label = ttk.Label(frame, background='#E4CCFF')
    img_label.grid(row=0, column=2, columnspan=2, pady=10)

    titulo = ttk.Label(frame, text="", font=("Arial", 16, "bold"), background='#E4CCFF', justify="center")
    titulo.grid(row=1, column=2, columnspan=2, pady=5)

    marca = ttk.Label(frame, text="", font=("Arial", 14, "bold"), background='#E4CCFF', justify="center")
    marca.grid(row=2, column=2, columnspan=2, pady=5)

    descripcion = ttk.Label(frame, text="", font=("Arial", 12), background='#E4CCFF', wraplength=400, justify="center")
    descripcion.grid(row=3, column=2, columnspan=2, pady=5)

    categoria = ttk.Label(frame, text="", font=("Arial", 12, "bold"), background='#E4CCFF', justify="center")
    categoria.grid(row=4, column=2, columnspan=2, pady=5)

    tags = ttk.Label(frame, text="", font=("Arial", 12), background='#E4CCFF', foreground='#666666', justify="center")
    tags.grid(row=5, column=2, columnspan=2, pady=5)

    sku = ttk.Label(frame, text="", font=("Arial", 12), background='#E4CCFF', justify="center")
    sku.grid(row=9, column=2, columnspan=2, pady=5)

    precio = ttk.Label(frame, text="", font=("Arial", 20, "bold"), background='#E4CCFF', justify="center")
    precio.grid(row=9, column=4, columnspan=2, pady=5)

    rating = ttk.Label(frame, text="", font=("Arial", 16, "bold"), background='#E4CCFF', justify="center")
    rating.grid(row=9, column=0, pady=5)

    stock = ttk.Label(frame, text="", font=("Arial", 12), background='#E4CCFF', justify="center")
    stock.grid(row=8, column=4, columnspan=2, pady=5)

    frame_botones = tk.Frame(frame, background='#E4CCFF')
    frame_botones.grid(row=12, column=2, columnspan=3, pady=20)

    boton_anterior = ttk.Button(frame_botones, text="Anterior", command=lambda: anterior(titulo, descripcion, categoria, precio, rating, stock, tags, marca, sku, img_label, lista_productos))
    boton_anterior.grid(row=0, column=1)

    boton_siguiente = ttk.Button(frame_botones, text="Siguiente", command=lambda: siguiente(titulo, descripcion, categoria, precio, rating, stock, tags, marca, sku, img_label, lista_productos))
    boton_siguiente.grid(row=0, column=3, padx=35)

    actualizar_producto(titulo, descripcion, categoria, precio, rating, stock, tags, marca, sku, img_label, lista_productos)

    ventanaProductos.mainloop()
