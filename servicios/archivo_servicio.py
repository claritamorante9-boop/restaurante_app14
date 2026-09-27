import json
import os

class ArchivoServicio:
    @staticmethod
    def leer_json(ruta):
        if not os.path.exists(ruta):
            return []
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
