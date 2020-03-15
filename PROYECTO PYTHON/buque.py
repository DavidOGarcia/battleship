from barco import Barco

class Buque(Barco):

    def __init__(self,posicion,tamaño,habilidad):
        self.habilidad = "permitir aterrizar helicópteros en él para el transporte de tropas."
        super().__init__(posicion,tamaño=3)

    def descripcion(self):
        
        return f"El buque es un barco de tamaño {self.tamaño} y tiene la habilidad de {self.habilidad}"