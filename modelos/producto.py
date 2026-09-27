class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "precio": self.precio}

    @classmethod
    def from_dict(cls, datos):
        return cls(datos["id"], datos["nombre"], datos["precio"])