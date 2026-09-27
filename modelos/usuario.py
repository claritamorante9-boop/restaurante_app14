class Usuario:
    def __init__(self, id, nombre, contrasena=""):
        self.id = id
        self.nombre = nombre
        self.contrasena = contrasena

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "contrasena": self.contrasena}

    @classmethod
    def from_dict(cls, datos):
        return cls(datos["id"], datos["nombre"], datos.get("contrasena", ""))