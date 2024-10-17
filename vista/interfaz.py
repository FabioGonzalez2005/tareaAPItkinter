import tkinter as tk
from tkinter import ttk

def mostrarProductos(lista_productos):
    ventanaProductos = tk.Tk()
    ventanaProductos.title("Productos de Fabio")
    ventanaProductos.geometry("400x400")

    titulos = ""
    for producto in lista_productos.products:
        titulos += producto.title

    mostrar_titulos = titulos + "\n"

    canvas = tk.Canvas(ventanaProductos, width=400, height=400)
    canvas.pack()

    titulo = ttk.Label(ventanaProductos, text=mostrar_titulos, background='lightgrey')
    canvas.create_window(200, 50, window=titulo)

    ventanaProductos.mainloop()


