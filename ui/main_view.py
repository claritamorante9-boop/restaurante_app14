import os
import tkinter as tk
from tkinter import ttk

class MainView:
    def __init__(self, ventana, servicio, usuario_actual=None):
        self.ventana = ventana
        self.servicio = servicio
        self.usuario_actual = usuario_actual
        self.ventana.title("Restaurante App — Sistema de Ventas")

        # === Cargar logo ===
        self.logo = None
        ruta_logo = os.path.join("assets", "logo.png")
        if os.path.exists(ruta_logo):
            try:
                from PIL import Image, ImageTk
                imagen_original = Image.open(ruta_logo)
                ancho_nuevo = imagen_original.width // 3
                alto_nuevo = imagen_original.height // 3
                imagen_redimensionada = imagen_original.resize(
                    (ancho_nuevo, alto_nuevo),
                    Image.Resampling.LANCZOS
                )
                self.logo = ImageTk.PhotoImage(imagen_redimensionada)
            except ImportError:
                print("Instala pillow: pip install pillow")
            except Exception as e:
                print(f"Logo no cargado: {e}")

        self._construir_interfaz()
        self._cargar_listas()

    def _construir_interfaz(self):
        marco = ttk.Frame(self.ventana, padding=15)
        marco.pack(fill="both", expand=True)

        if self.logo:
            ttk.Label(marco, image=self.logo).pack(pady=10)

        cuaderno = ttk.Notebook(marco)
        cuaderno.pack(fill="both", expand=True)

        p_ventas = ttk.Frame(cuaderno, padding=10)
        cuaderno.add(p_ventas, text="Registrar Venta")

        form = ttk.Frame(p_ventas)
        form.pack(fill="both", expand=True)

        ttk.Label(form, text="Usuario:").grid(row=0, column=0, sticky="w", pady=5)
        self.cmb_usuario = ttk.Combobox(form, state="readonly", width=35)
        self.cmb_usuario.grid(row=0, column=1, pady=5)

        ttk.Label(form, text="Producto:").grid(row=1, column=0, sticky="w", pady=5)
        self.cmb_producto = ttk.Combobox(form, state="readonly", width=35)
        self.cmb_producto.grid(row=1, column=1, pady=5)

        ttk.Label(form, text="Cantidad:").grid(row=2, column=0, sticky="w", pady=5)
        self.ent_cantidad = ttk.Entry(form, width=38)
        self.ent_cantidad.grid(row=2, column=1, pady=5)

        ttk.Button(form, text="Registrar Venta",
                   command=self._registrar_venta).grid(row=3, column=0, columnspan=2, pady=10)

        ttk.Label(form, text="Historial de Ventas:").grid(row=4, column=0, columnspan=2, sticky="w", pady=(15, 5))
        columnas = ("usuario", "producto", "cantidad", "fecha")
        self.tabla = ttk.Treeview(form, columns=columnas, show="headings", height=8)
        for col in columnas:
            self.tabla.heading(col, text=col.title())
            self.tabla.column(col, width=160)
        self.tabla.grid(row=5, column=0, columnspan=2, sticky="nsew")

        form.grid_columnconfigure(1, weight=1)
        form.grid_rowconfigure(5, weight=1)

    def _cargar_listas(self):
        usuarios = self.servicio.obtener_usuarios()
        self.cmb_usuario["values"] = [u.nombre for u in usuarios]
        if usuarios:
            self.cmb_usuario.current(0)

        productos = self.servicio.obtener_productos()
        self.cmb_producto["values"] = [f"{p.nombre} - ${p.precio}" for p in productos]
        if productos:
            self.cmb_producto.current(0)

        self._actualizar_tabla()

    def _registrar_venta(self):
        try:
            cant = int(self.ent_cantidad.get())
            if cant <= 0:
                return
            i_u = self.cmb_usuario.current()
            i_p = self.cmb_producto.current()
            if i_u < 0 or i_p < 0:
                return

            usuarios = self.servicio.obtener_usuarios()
            productos = self.servicio.obtener_productos()
            usuario = usuarios[i_u]
            producto = productos[i_p]

            self.servicio.registrar_venta(usuario.id, producto.id, cant)
            self.ent_cantidad.delete(0, "end")
            self._actualizar_tabla()
        except ValueError:
            pass

    def _actualizar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        usuarios = {u.id: u.nombre for u in self.servicio.obtener_usuarios()}
        productos = {p.id: p.nombre for p in self.servicio.obtener_productos()}
        for v in self.servicio.obtener_ventas():
            self.tabla.insert("", "end", values=(
                usuarios.get(v.usuario_id, "Desconocido"),
                productos.get(v.producto_id, "Desconocido"),
                v.cantidad,
                v.fecha
            ))