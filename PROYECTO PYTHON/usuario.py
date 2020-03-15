class Usuario:
    def __init__(self, username, nombre, edad, genero, puntaje = 0,disparos=0):
        self.username = username
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.puntaje = int(puntaje)
        self.disparos = disparos

    def __str__(self):
        return 'Usuario: {}\nNombre completo: {}\nEdad: {}\nGenero: {}\nPuntaje: {}\nDisparos:{}\n'.format(self.username, self.nombre, self.edad, self.genero,self.puntaje,self.disparos)