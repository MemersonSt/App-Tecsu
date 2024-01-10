import tkinter as tk
from controls.api import get_data


class PanelPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tecsup")
        self.geometry("800x600")
        self.resizable(False, False)
        self.create_widgets()
        self.get_products()

    def create_widgets(self):
        self.label = tk.Label(self, text="Productos")
        self.label.grid(row=0, column=0)

        self.listbox = tk.Listbox(self)
        self.listbox.grid(row=1, column=0)

    def get_products(self):
        products = get_data()
        if products:
            for product in products:
                self.listbox.insert(tk.END, product['name'])
        else:
            self.listbox.insert(tk.END, "No hay productos")


