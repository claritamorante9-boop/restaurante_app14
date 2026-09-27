from datetime import datetime

class Venta:
    def __init__(self, usuario_id, producto_id, cantidad, fecha=None):
        self.usuario_id = usuario_id
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.fecha = fecha if fecha else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "usuario_id": self.usuario_id,
            "producto_id": self.producto_id,
            "cantidad": self.cantidad,
            "fecha": self.fecha
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(
            datos["usuario_id"],
            datos["producto_id"],
            datos["cantidad"],
            datos.get("fecha")
        )