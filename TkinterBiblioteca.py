import tkinter as tk
from tkinter import ttk, messagebox

class Autor:
    def __init__(self, nombre, ):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.prestado_a = None

    def prestar(self, usuario):
        if self.prestado_a:
            messagebox.showinfo("Error", f"El libro {self.titulo} ya está prestado a {self.prestado_a}")
        else:
            self.prestado_a = usuario
            messagebox.showinfo("Éxito", f"El libro {self.titulo} ha sido prestado a {usuario}")

    def devolver(self):
        if self.prestado_a:
            messagebox.showinfo("Éxito", f"El libro {self.titulo} ha sido devuelto")
            self.prestado_a = None
        else:
            messagebox.showinfo("Error", f"El libro {self.titulo} no estaba prestado")

def prestar_libro():
    libro = libros[libro_combobox.current()]
    usuario = usuario_entry.get()
    libro.prestar(usuario)

def devolver_libro():
    libro = libros[libro_combobox.current()]
    libro.devolver()

def agregar_libro():
    titulo = nuevo_titulo_entry.get()
    autor_nombre = nuevo_autor_nombre_entry.get()
    autor_apellido = nuevo_autor_apellido_entry.get()
    isbn = nuevo_isbn_entry.get()

    autor = Autor(autor_nombre, autor_apellido)
    libro = Libro(titulo, autor, isbn)
    libros.append(libro)

    libro_combobox['values'] = [libro.titulo for libro in libros]
    messagebox.showinfo("Éxito", "Libro agregado correctamente")

# Crear objetos
autor1 = Autor("Stephen", "King")
autor2 = Autor("J.K.", "Rowling")

libros = [
    Libro("It", autor1, "978-1501156687"),
    Libro("Harry Potter", autor2, "978-0590353427")
]

# Configurar interfaz gráfica
root = tk.Tk()
root.title("Sistema de Biblioteca")

# Widgets
label_libro = tk.Label(root, text="Libro:")
label_libro.grid(row=0, column=0, padx=10, pady=5)
libro_combobox = ttk.Combobox(root, values=[libro.titulo for libro in libros])
libro_combobox.grid(row=0, column=1, padx=10, pady=5)

label_usuario = tk.Label(root, text="Usuario:")
label_usuario.grid(row=1, column=0, padx=10, pady=5)
usuario_entry = tk.Entry(root)
usuario_entry.grid(row=1, column=1, padx=10, pady=5)

prestar_button = tk.Button(root, text="Prestar Libro", command=prestar_libro)
prestar_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="WE")

devolver_button = tk.Button(root, text="Devolver Libro", command=devolver_libro)
devolver_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="WE")

# Widgets para agregar libros
nuevo_titulo_label = tk.Label(root, text="Nuevo Título:")
nuevo_titulo_label.grid(row=4, column=0, padx=10, pady=5)
nuevo_titulo_entry = tk.Entry(root)
nuevo_titulo_entry.grid(row=4, column=1, padx=10, pady=5)

nuevo_autor_nombre_label = tk.Label(root, text="Nombre del Autor:")
nuevo_autor_nombre_label.grid(row=5, column=0, padx=10, pady=5)
nuevo_autor_nombre_entry = tk.Entry(root)
nuevo_autor_nombre_entry.grid(row=5, column=1, padx=10, pady=5)

nuevo_autor_apellido_label = tk.Label(root, text="Apellido del Autor:")
nuevo_autor_apellido_label.grid(row=6, column=0, padx=10, pady=5)
nuevo_autor_apellido_entry = tk.Entry(root)
nuevo_autor_apellido_entry.grid(row=6, column=1, padx=10, pady=5)

nuevo_isbn_label = tk.Label(root, text="ISBN:")
nuevo_isbn_label.grid(row=7, column=0, padx=10, pady=5)
nuevo_isbn_entry = tk.Entry(root)
nuevo_isbn_entry.grid(row=7, column=1, padx=10, pady=5)

agregar_libro_button = tk.Button(root, text="Agregar Libro", command=agregar_libro)
agregar_libro_button.grid(row=8, column=0, columnspan=2, padx=10, pady=5, sticky="WE")

root.mainloop()
