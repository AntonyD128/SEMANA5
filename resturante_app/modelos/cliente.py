class Cliente: 
    def __init__ (self, 
        nombre: str,
        email: str,
        telefono: str,
        edad: None,
        mayor_de_edad: bool = True):

        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.edad = edad
        self.mayor_de_edad = mayor_de_edad


    def mostrar_informacion (self): 
        return f"Nombre: {self.nombre} | Email: {self.email} | Telefono: {self.telefono} | Edad: {self.edad} | Mayor de edad: {'Sí' if self.mayor_de_edad else 'No'}"


    def __str__(self):
        texto_mayor = 'Sí' if self.mayor_de_edad else 'No'
        return f"Nombre: {self.nombre} | Email: {self.email} | Telefono: {self.telefono} | Edad: {self.edad} | Mayor de edad: {texto_mayor}"