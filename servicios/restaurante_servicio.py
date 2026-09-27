from modelos import Usuario, Producto, Venta
import json
import os

class RestauranteServicio:
    def __init__(self):
        self.usuarios = []
        self.productos = []
        self.ventas = []
        self._cargar_datos()

    def _cargar_datos(self):
        ruta_usuarios = os.path.join("datos", "usuarios.json")
        if os.path.exists(ruta_usuarios):
            with open(ruta_usuarios, "r", encoding="utf-8") as f:
                datos = json.load(f)
                self.usuarios = [Usuario.from_dict(u) for u in datos]

        ruta_productos = os.path.join("datos", "productos.json")
        if os.path.exists(ruta_productos):
            with open(ruta_productos, "r", encoding="utf-8") as f:
                datos = json.load(f)
                self.productos = [Producto.from_dict(p) for p in datos]

        self._cargar_ventas()

    def validar_acceso(self, nombre_usuario, contrasena):
        for usuario in self.usuarios:
            if hasattr(usuario, 'contrasena'):
                if usuario.nombre == nombre_usuario and usuario.contrasena == contrasena:
                    return usuario
            else:
                if usuario.nombre == nombre_usuario:
                    return usuario
        return None

    def obtener_usuarios(self):
        return self.usuarios

    def obtener_productos(self):
        return self.productos

    def obtener_ventas(self):
        return self.ventas

    def _cargar_ventas(self):
        ruta = os.path.join("datos", "ventas.json")
        if os.path.exists(ruta):
            with open(ruta, "r", encoding="utf-8") as f:
                datos = json.load(f)
                self.ventas = [Venta.from_dict(v) for v in datos]

    def _guardar_ventas(self):
        ruta = os.path.join("datos", "ventas.json")
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump([v.to_dict() for v in self.ventas], f, ensure_ascii=False, indent=2)

    def registrar_venta(self, usuario_id, producto_id, cantidad, fecha=None):
        nueva_venta = Venta(usuario_id, producto_id, cantidad, fecha)
        self.ventas.append(nueva_venta)
        self._guardar_ventas()
        return nueva_venta