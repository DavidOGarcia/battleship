from barco import Barco

class Fragata(Barco):

    def __init__(self,posicion,tamaño,habilidad):
        self.habilidad = "comunicarse con tierra y los otros miembros de la flota."
        super().__init__(posicion,tamaño=2)

    def descripcion(self):
        
        return f"La fragata es un barco de tamaño {self.tamaño} y tiene la habilidad de {self.habilidad}"