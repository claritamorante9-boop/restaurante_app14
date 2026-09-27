class Usuario:
    def __init__(self, id, usuario, contrasena, nombre):
        self.id = id
        self.usuario = usuario
        self.contrasena = contrasena
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre} ({self.usuario})"


        

