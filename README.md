PROGRMA CREADO POR :
Antony Jordano Defaz Diaz

SISTEMA DE GESTION DEL RESTAURANTE

📝 Descripción del Proyecto
Este proyecto consiste en una aplicación de consola desarrollada en Python aplicando el paradigma de Programación Orientada a Objetos (POO) y una arquitectura modular. El sistema permite administrar el menú de productos (con información nutricional y comercial) y el registro de clientes de un restaurante, organizando el código en módulos separados para garantizar un mantenimiento limpio, estructurado y escalable.

📂 Estructura del Proyecto
El código se organiza de forma modular dividiendo las clases según su responsabilidad dentro del sistema:

restaurante_app/
│
├── modelos/
│   ├── __init__.py      # Inicializador del paquete de modelos
│   ├── cliente.py       # Definición de la clase Cliente (nombre, email, teléfono, edad)
│   └── producto.py      # Definición de la clase Producto (nombre, precio, calorías, etc.)
│
├── servicios/
│   ├── __init__.py      # Inicializador del paquete de servicios
│   └── restaurante.py   # Lógica de control del Restaurante (listas de productos y clientes)
│
└── main.py              # Punto de entrada principal para ejecutar el programa


🛠️ Funcionalidades del Sistema
Crear objetos de tipo Producto: Instancia alimentos y bebidas registrando su nombre, stock disponible, precio de venta y su aporte en calorías.

Crear objetos de tipo Cliente: Registra a los consumidores asignándoles sus datos de contacto y validando de forma interna su rango de edad.

Registrar productos en el menú: Agrega los objetos Producto dentro del inventario del restaurante usando colecciones dinámicas.

Registrar clientes en el sistema: Incorpora de manera ordenada los objetos Cliente a la lista de usuarios del establecimiento.

Mostrar información estructurada: Genera reportes formateados y legibles en consola con todo el menú de productos y la lista de clientes registrados.

🧠 Conceptos Técnicos Aplicados
### Identificadores Descriptivos
Siguiendo las buenas prácticas de la guía de estilo PEP 8, se utilizan nombres claros y autoexplicativos en español para identificar cada componente:

Clases (PascalCase): Producto, Cliente, Restaurante.

Atributos y Variables (snake_case): nombre, cantidad, precio, calorias, disponible, email, telefono, edad, mayor_de_edad.

Métodos (snake_case): agregar_producto(), agregar_cliente(), mostrar_producto(), mostrar_cliente().

### Tipos de Datos

Durante el desarrollo del programa se utilizan diferentes tipos de datos:

| Tipo | Ejemplo |
| :--- | :--- |
| `str` | nombre, email, telefono |
| `int` | cantidad, calorias, edad |
| `float`| precio |
| `bool` | disponible, mayor_de_edad |


