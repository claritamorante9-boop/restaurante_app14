#  Restaurante App — Sistema de Ventas
**Semana 15** — Proyecto de Registro y Gestión de Ventas

##  Descripción
Aplicación de escritorio desarrollada en Python con Tkinter para el registro de ventas de un restaurante. Permite iniciar sesión, seleccionar productos, registrar ventas y visualizar el historial completo con fecha y hora. Los datos se guardan automáticamente en archivos JSON.

## Funcionalidades
-  Inicio de sesión con usuario y contraseña
-  Selección de usuario
-  Catálogo de productos con precios
-  Registro de ventas con cantidad
-  Historial de ventas en tabla con:
  - Usuario
  - Producto
  - Cantidad
  - Fecha y hora
-  Guardado automático en archivos JSON
-  Logo personalizado de la aplicación
-  Carga de datos persistente al abrir la app

##  Tecnologías
- **Python 3**
- **Tkinter** — Interfaz gráfica
- **Pillow** — Manejo de imágenes
- **JSON** — Almacenamiento de datos

##  Estructura del Proyecto
restaurante-app-semana15/
├── assets/
│ └── logo.png
├── datos/
│ ├── usuarios.json
│ ├── productos.json
│ └── ventas.json
├── modelos/
│ ├── init.py
│ ├── usuario.py
│ ├── producto.py
│ └── venta.py
├── servicios/
│ ├── init.py
│ └── restaurante_servicio.py
├── ui/
│ ├── init.py
│ ├── login_view.py
│ └── main_view.py
├── main.py
└── README.md

#Instalación y Ejecución

 1. Instalar dependencias
```bash
pip install pillow
python main.py
3. Credenciales de acceso
Usuario: admin
Contraseña: 1234