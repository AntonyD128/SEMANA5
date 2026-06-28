from modelos.cliente import Cliente
from modelos.producto import Producto
from servicios.restaurante import Restaurante

mi_restaurante = Restaurante()

print("Bienvenido_al_sistema _de_pedidos_del_restaurante")

p1 = Producto("Hamburguesa", 5, 5.99, 300)
p2 = Producto("hotdog", 3, 3.99, 200)
p3 = Producto("Pizza", 2, 8.99, 400)


cliente1 = Cliente("Ana Armijos", "ana@gmail.com", "0981530189", 25)
cliente2 = Cliente("Carlos Perez", "carlos@gmail.com", "0987654321", 30)
cliente3 = Cliente("Maria Gomez", "maria@gmail.com", "0987654321", 28)

mi_restaurante.agregar_producto(p1)
mi_restaurante.agregar_producto(p2)
mi_restaurante.agregar_producto(p3)


mi_restaurante.agregar_cliente(cliente1)
mi_restaurante.agregar_cliente(cliente2)
mi_restaurante.agregar_cliente(cliente3)



mi_restaurante.mostrar_producto()
mi_restaurante.mostrar_cliente()
