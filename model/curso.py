class Curso:
    def __init__(self,nombre,codigo,credito):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__credito=credito

    def set_codigo(self, codigo):
        self.__codigo=codigo
    
    def set_nombre(self,nombre):
        self.__nombre=nombre
    
    def set_credito(self, credito):
        self.__credito=credito
    
    def get_codigo(self):
        return self.__codigo
    
    def get_nombre(self):
        return self.__nombre
    
    def get_credito(self):
        self.__credito

    def mostrar(self):
        print(f"Bienvenido al curso {self.__nombre} y tengo {self.__credito} creditos")