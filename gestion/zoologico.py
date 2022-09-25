from gestion.zona import Zona
class Zoologico:
    def __init__(self, nombre, ubicacion, zonas=[]):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = zonas

    def agregarZonas(self, zona):
        self._zonas.append(zona)

    def cantidadTotalAnimales(self):
        cont = 0
        for i in self._zona:
            cont += Zona.cantidadAnimales()
        return cont

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def getZona(self):
        return self._nombre
    
    def setZona(self, zona):
        self._zonas = zona


    
