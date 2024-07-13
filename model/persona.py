class Persona:
    def __init__(self,nombre,apellido,dni,email):
        self.nombre=nombre
        self.apellido=apellido
        self.email=email
        self.dni=dni
    
    def saludar(self):
        print(f"Hola soy el objeto {self.nombre}")
        