import tkinter as tk
from tkinter import messagebox

class MaquinaExpendedora:
    def __init__(self, root):
        self.root = root
        self.root.title("Máquina Expendedora")
        
        # Inicializar productos disponibles
        self.productos = {
            "001": {"nombre": "Producto 1", "precio": 2.50},
            "002": {"nombre": "Producto 2", "precio": 3.00},
            "003": {"nombre": "Producto 3", "precio": 4.00},
            "004": {"nombre": "Producto 4", "precio": 5.00}
        }
        
        # Inicializar variables de control
        self.codigo_producto = tk.StringVar()
        self.cantidad_dinero = tk.DoubleVar()
        self.cantidad_dinero.set(0.0)
        
        # Etiqueta para mostrar el saldo actual
        self.lbl_saldo = tk.Label(root, text="Saldo: $0.00")
        self.lbl_saldo.pack()
        
        # Entrada de texto para ingresar el código del producto
        self.entry_codigo_producto = tk.Entry(root, textvariable=self.codigo_producto)
        self.entry_codigo_producto.pack()
        
        # Botón para seleccionar el producto
        self.btn_seleccionar_producto = tk.Button(root, text="Seleccionar Producto", command=self.seleccionar_producto)
        self.btn_seleccionar_producto.pack()
        
        # Botones para agregar dinero
        self.btn_agregar_dinero_1 = tk.Button(root, text="Agregar $1.00", command=lambda: self.agregar_dinero(1.00))
        self.btn_agregar_dinero_1.pack()
        
        self.btn_agregar_dinero_5 = tk.Button(root, text="Agregar $5.00", command=lambda: self.agregar_dinero(5.00))
        self.btn_agregar_dinero_5.pack()
        
        self.btn_agregar_dinero_10 = tk.Button(root, text="Agregar $10.00", command=lambda: self.agregar_dinero(10.00))
        self.btn_agregar_dinero_10.pack()
        
        # Botón para comprar producto
        self.btn_comprar_producto = tk.Button(root, text="Comprar Producto", command=self.comprar_producto)
        self.btn_comprar_producto.pack()
        
    def seleccionar_producto(self):
        codigo = self.codigo_producto.get()
        if codigo in self.productos:
            producto = self.productos[codigo]
            messagebox.showinfo("Producto Seleccionado", f"Producto: {producto['nombre']}, Precio: ${producto['precio']:.2f}")
        else:
            messagebox.showerror("Error", "Código de producto inválido.")
        
    def agregar_dinero(self, cantidad):
        self.cantidad_dinero.set(self.cantidad_dinero.get() + cantidad)
        self.actualizar_saldo()
        
    def actualizar_saldo(self):
        self.lbl_saldo.config(text="Saldo: ${:.2f}".format(self.cantidad_dinero.get()))
        
    def comprar_producto(self):
        codigo = self.codigo_producto.get()
        if codigo in self.productos:
            producto = self.productos[codigo]
            if self.cantidad_dinero.get() >= producto['precio']:
                messagebox.showinfo("Compra Exitosa", f"¡Producto {producto['nombre']} comprado!")
                self.cantidad_dinero.set(self.cantidad_dinero.get() - producto['precio'])
                self.actualizar_saldo()
            else:
                messagebox.showerror("Saldo Insuficiente", "No tienes suficiente dinero para comprar el producto.")
        else:
            messagebox.showerror("Error", "Código de producto inválido.")

if __name__ == "__main__":
    root = tk.Tk()
    maquina = MaquinaExpendedora(root)
    root.mainloop()






