import tkinter as tk
from tkinter import messagebox

class LoginView:
    def __init__(self, ventana, servicio, on_success):
        self.ventana = ventana
        self.servicio = servicio
        self.on_success = on_success
        self.frame = tk.Frame(ventana, bg="#f0f0f0")
        self.frame.pack(expand=True)

        contenedor = tk.Frame(self.frame, bg="white", bd=2, relief="groove")
        contenedor.pack(padx=40, pady=40)

        tk.Label(contenedor, text="Restaurante App", font=("Arial", 18, "bold"), bg="white").pack(pady=(20, 10))
        tk.Label(contenedor, text="Iniciar Sesión", font=("Arial", 12), bg="white").pack(pady=(0, 20))

        tk.Label(contenedor, text="Usuario", bg="white").pack()
        self.entrada_usuario = tk.Entry(contenedor, width=30)
        self.entrada_usuario.pack(pady=(0, 10))

        tk.Label(contenedor, text="Contraseña", bg="white").pack()
        self.entrada_contrasena = tk.Entry(contenedor, width=30, show="*")
        self.entrada_contrasena.pack(pady=(0, 20))

        tk.Button(contenedor, text="Ingresar", width=20, command=self._ingresar).pack(pady=(0, 10))

    def _ingresar(self):
        usuario = self.entrada_usuario.get().strip()
        contrasena = self.entrada_contrasena.get().strip()
        u = self.servicio.validar_acceso(usuario, contrasena)
        if u:
            self.on_success(u)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    def destruir(self):
        self.frame.destroy()
