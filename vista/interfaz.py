import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests

indice_actual = 0


def actualizar_producto(titulo_label, descripcion_label, categoria_label, precio_label, rating_label, stock_label, tags_label, marca_label, sku_label, img_label, lista_productos):
    producto = lista_productos.products[indice_actual]

    titulo_label.config(text=producto.title)
    descripcion_label.config(text=producto.description)
    categoria_label.config(text=producto.category)
    precio_label.config(text=producto.price)
    rating_label.config(text=producto.rating)
    stock_label.config(text=producto.stock)
    tags_label.config(text=f"Tags: #{', #'.join(producto.tags)}")
    marca_label.config(text=producto.brand)
    sku_label.config(text=producto.sku)

    response = requests.get(producto.thumbnail, stream=True)
    img_data = response.raw
    img = Image.open(img_data)
    img.thumbnail((200, 200))
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
    ventanaProductos.geometry("500x600")

    canvas = tk.Canvas(ventanaProductos, width=500, height=600, background='#E4CCFF')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    frame = tk.Frame(canvas, background='#E4CCFF')
    canvas.create_window((0, 0), window=frame, anchor='nw')

    titulo = ttk.Label(frame, text="", font=("Arial", 16), background='#E4CCFF')
    titulo.pack(pady=5)

    descripcion = ttk.Label(frame, text="", font=("Arial", 12), background='#E4CCFF')
    descripcion.pack(pady=5)

    categoria = ttk.Label(frame, text="", font=("Arial", 12), background='#E4CCFF')
    categoria.pack(pady=5)

    precio = ttk.Label(frame, text="", font=("Arial", 12), background='#E4CCFF')
    precio.pack(pady=5)

    rating = ttk.Label(frame, text="", font=("Arial", 12), background='#E4CCFF')
    rating.pack(pady=5)

    stock = ttk.Label(frame, text="", font=("Arial", 12), background='#E4CCFF')
    stock.pack(pady=5)

    tags = ttk.Label(frame, text="", font=("Arial", 12), background='#E4CCFF')
    tags.pack(pady=5)

    marca = ttk.Label(frame, text="", font=("Arial", 12), background='#E4CCFF')
    marca.pack(pady=5)

    sku = ttk.Label(frame, text="", font=("Arial", 12), background='#E4CCFF')
    sku.pack(pady=5)

    img_label = ttk.Label(frame, background='#E4CCFF')
    img_label.pack(pady=10)

    frame_botones = tk.Frame(frame, background='#E4CCFF')
    frame_botones.pack(pady=20)

    boton_anterior = ttk.Button(frame_botones, text="Anterior", command=lambda: anterior(titulo, descripcion, categoria, precio, rating, stock, tags, marca, sku, img_label, lista_productos))
    boton_anterior.pack(side=tk.LEFT, padx=10)

    boton_siguiente = ttk.Button(frame_botones, text="Siguiente", command=lambda: siguiente(titulo, descripcion, categoria, precio, rating, stock, tags, marca, sku, img_label, lista_productos))
    boton_siguiente.pack(side=tk.RIGHT, padx=10)

    actualizar_producto(titulo, descripcion, categoria, precio, rating, stock, tags, marca, sku, img_label, lista_productos)

    ventanaProductos.mainloop()
