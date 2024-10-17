import tkinter as tk
from tkinter import ttk

main_window = tk.Tk()
main_window.title("Lista de productos")
treeview = ttk.Treeview(columns=("size", "lastmod"))
treeview.heading("#0", text="Titulo")
treeview.heading("size", text="Tamaño")
treeview.heading("lastmod", text="Última modificación")
treeview.insert(
    "",
    tk.END,
    text="README.txt",
    values=("850 bytes", "18:30")
)
treeview.pack()
main_window.mainloop()