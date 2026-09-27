import tkinter as tk
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Restaurante App")
        self.ventana.geometry("800x600")
        self.servicio = RestauranteServicio()
        self.usuario = None
        self.login_view = None
        self.main_view = None
        self._mostrar_login()

    def _mostrar_login(self):
        if self.main_view:
            self.main_view.destruir()
            self.main_view = None
        self.login_view = LoginView(self.ventana, self.servicio, self._on_login_success)
        self.login_view.frame.pack(fill="both", expand=True)

    def _on_login_success(self, usuario):
        self.usuario = usuario
        self.login_view.destruir()
        self.login_view = None
        self.main_view = MainView(self.ventana, self.servicio, self.usuario, self._mostrar_login)
        self.main_view.frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = App(ventana)
    ventana.mainloop()
