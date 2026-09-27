import tkinter as tk


class MainView:
    def __init__(self, ventana, servicio, usuario, on_logout):
        self.servicio = servicio
        self.usuario = usuario
        self.on_logout = on_logout

        self.frame = tk.Frame(ventana, bg="#f0f0f0")
        self.frame.pack(fill="both", expand=True)

        # Barra superior
        cabecera = tk.Frame(self.frame, bg="#2c3e50")
        cabecera.pack(fill="x")
        tk.Label(cabecera, text=f"Restaurante App - {usuario.nombre}", fg="white", bg="#2c3e50", font=("Arial", 14, "bold")).pack(side="left", padx=10, pady=10)
        tk.Button(cabecera, text="Cerrar sesión", bg="#e74c3c", fg="white", command=self.on_logout).pack(side="right", padx=10, pady=10)

        # Contenedor principal
        principal = tk.Frame(self.frame, bg="#f0f0f0")
        principal.pack(fill="both", expand=True, padx=10, pady=10)

        # Panel de navegación (izquierda)
        nav = tk.Frame(principal, bg="#ecf0f1", width=180)
        nav.pack(side="left", fill="y")
        nav.pack_propagate(False)
        tk.Label(nav, text="Navegación", bg="#ecf0f1", font=("Arial", 12, "bold")).pack(pady=(15, 10))
        tk.Button(nav, text="Productos", width=18, command=self.mostrar_productos).pack(pady=5)
        tk.Button(nav, text="Usuarios", width=18, command=self.mostrar_usuarios).pack(pady=5)

        # Panel de contenido (derecha)
        self.contenido = tk.Frame(principal, bg="white", bd=1, relief="solid")
        self.contenido.pack(side="left", fill="both", expand=True, padx=10)

        self.texto = tk.Text(self.contenido, width=50, height=15)
        self.texto.pack(padx=10, pady=10)

    def mostrar_productos(self):
        self.texto.delete("1.0", tk.END)
        for p in self.servicio.listar_productos():
            self.texto.insert(tk.END, f"{p.id}. {p.nombre} - ${p.precio} - {p.cantidad} uds\n")

    def mostrar_usuarios(self):
        self.texto.delete("1.0", tk.END)
        for u in self.servicio.listar_usuarios():
            self.texto.insert(tk.END, f"{u.id}. {u.nombre} ({u.usuario})\n")

    def destruir(self):
        self.frame.destroy()
