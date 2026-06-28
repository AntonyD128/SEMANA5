class Restaurante:
    def __init__(self):

        # Aquí inicializamos las listas vacías para que existan
        self.clientes = []
        self.productos = []

    def agregar_cliente(self, cliente):
        # Corregido el espacio y ahora añadimos la variable 'cliente'
        self.clientes.append(cliente)

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_cliente(self):
        print("CLIENTES:")
        for cliente in self.clientes:
            print(cliente)

    def mostrar_producto(self):
        print("PRODUCTOS:")
        for producto in self.productos:
            print(producto)