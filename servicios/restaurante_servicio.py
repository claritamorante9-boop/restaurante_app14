import os
from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self):
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.ruta_usuarios = os.path.join(base, "datos", "usuarios.json")
        self.ruta_productos = os.path.join(base, "datos", "productos.json")
        self.usuarios = self._cargar_usuarios()
        self.productos = self._cargar_productos()

    def _cargar_usuarios(self):
        datos = ArchivoServicio.leer_json(self.ruta_usuarios) or []
        return [Usuario(u["id"], u["usuario"], u["contrasena"], u["nombre"]) for u in datos]

    def _cargar_productos(self):
        datos = ArchivoServicio.leer_json(self.ruta_productos) or []
        return [Producto(p["id"], p["nombre"], p["precio"], p["cantidad"]) for p in datos]

    def _guardar_productos(self):
        datos = [{"id": p.id, "nombre": p.nombre, "precio": p.precio, "cantidad": p.cantidad} for p in self.productos]
        ArchivoServicio.escribir_json(self.ruta_productos, datos)



    def validar_acceso(self, usuario, contrasena):
        for u in self.usuarios:
            if u.usuario == usuario and u.contrasena == contrasena:
                return u
        return None

    def listar_usuarios(self):
        return self.usuarios

    def listar_productos(self):
        return self.productos

    def registrar_producto(self, nombre, precio, cantidad):
        try:
            precio = float(precio)
            cantidad = int(cantidad)
        except ValueError:
            return False,"Precio y cantidad deben ser numéricos"
        if not nombre.strip():
            return False,"El nombre no puede estar vacío"
        nuevo_id = max([p.id for p in self.productos], default=0) + 1
        self.productos.append(Producto(nuevo_id, nombre.strip(), precio, cantidad))
        self._guardar_productos()
        return True,f"Producto '{nombre}' registrado con ID {nuevo_id}"

    def consultar_producto(self, pid):
        for p in self.productos:

            if p.id == pid:
                return True,f"{p.id}. {p.nombre} - ${p.precio} - {p.cantidad} uds"
  
