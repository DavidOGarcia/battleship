from barco import Barco

class Submarino(Barco):
    def __init__(self,posicion,tamaño,habilidad):
        self.habilidad = "sumergirse y emerger del agua."
        super().__init__(posicion,tamaño=1)

    def descripcion(self):
        
        return f"El submarino es un barco de tamaño {self.tamaño} y tiene la habilidad de {self.habilidad}"