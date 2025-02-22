class Equipo:
    def __init__(self, nombre, puntos, gfavor, gcontra):
        self.nombre = nombre
        self.puntos = puntos
        self.gfavor = gfavor
        self.gcontra = gcontra
        self.gdif = gfavor - gcontra

class Partido:
    def __init__(self, local, glarin, grival):
        self.local = local
        self.glarin = glarin
        self.grival = grival
    
class Jugador:
    def __init__(self, nombre, dorsal, posicion, goles):
        self.nombre = nombre
        self.dorsal = dorsal
        self.posicion = posicion
        self.goles = goles