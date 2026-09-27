 Restaurante App — Semana 14

Aplicación de gestión de un restaurante con interfaz gráfica (Tkinter/ttk). Esta versión corresponde a la **Semana 14**, donde se evoluciona la capa de interfaz mediante **componentes y contenedores**, incorporando formularios, tablas y operaciones CRUD sobre productos, manteniendo la arquitectura modular y la persistencia en archivos JSON.

 #Estructura del proyecto
 restaurante_app/ ├── datos/ │ ├── productos.json │ └── usuarios.json ├── modelos/ │ ├── init.py │ ├── producto.py │ └── usuario.py ├── servicios/ │ ├── init.py │ ├── archivo_servicio.py │ └── restaurante_servicio.py ├── ui/ │ ├── init.py │ ├── login_view.py │ └── main_view.py └── main.py

## Componentes y contenedores utilizados

- **Contenedores**: `Frame` para separar barra superior, panel de navegación y panel de contenido; `LabelFrame` implícito mediante secciones organizadas.
- **Componentes**: `Label`, `Entry`, `Button`, `Treeview` (tabla), `Combobox` no utilizado por simplicidad.
- **Gestores de geometría**: `pack` para organización general y `grid` dentro del formulario de productos.

## Operaciones sobre productos

- **Registrar**: añade un nuevo producto y guarda en `productos.json`.
- **Consultar**: busca un producto por su ID y muestra su información.
- **Actualizar**: modifica nombre, precio y cantidad de un producto existente.
- **Eliminar**: elimina un producto por su ID y guarda los cambios.


Todas las operaciones se delegan a `RestauranteServicio`, que valida y persiste mediante `ArchivoServicio`.

## Persistencia

Los productos se guardan en `datos/productos.json` a través del servicio correspondiente, por lo que los cambios se conservan al cerrar y volver a ejecutar la aplicación.



## Ejecución

Requisito: tener Python instalado.



```bash
python main.py


