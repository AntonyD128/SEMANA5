class Producto: 
    def __init__(self,
        
        nombre: str,
        cantidad: int,
        precio: float,
        calorias: int,
        disponible: bool = True):

        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.calorias = calorias
        self.disponible = disponible

    def mostrar_informacion (self): 
        disponibilidad = "Disponible" if self.disponible else "No disponible"
        return f"Nombre: {self.nombre}\nCantidad: {self.cantidad}\nPrecio: {self.precio}\nCalorías: {self.calorias}\nDisponibilidad: {disponibilidad}"

    def __str__(self):
        return self.mostrar_informacion()