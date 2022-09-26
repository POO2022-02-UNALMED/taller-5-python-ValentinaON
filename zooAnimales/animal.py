from gestion.zona import Zona
class Animal:
    _totalAnimales = 0
    def __init__(self, nombre, edad, habitat, genero, zonas = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zonas = zonas
        Animal._totalAnimales += 1
  
    def movimiento():
        return "desplazarse"

    @classmethod
    def totalPorTipo():
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        return "Mamiferos: "+Mamifero.cantidadMamiferos()+'\n'+"Aves: "+Ave.cantidadAves()+'\n'+"Reptiles: "+Reptil.cantidadReptiles()+'\n'+"Peces: " + Pez.cantidadPeces()+'\n'+"Anfibios: " + Anfibio.cantidadAnfibios()


    def toString(self):
        if self._zonas != None:
             return "Mi nombre es " + self._nombre +", tengo una edad de " + str (self._edad) +", habito en " + self._habitat +" y mi genero es " + self._genero
        else:
             return "Mi nombre es " + self._nombre +", tengo una edad de " + self._edad +", habito en " + self._habitat +" y mi genero es " + self._genero +", la zona en la que me ubico es " + self._zonas +", en el " + self._zonas.getZoo();

    @classmethod   
    def getTotalAnimales(cls):
        return cls._totalAnimales

    @classmethod
    def setTotalAnimales(cls, totalAnimales):
        cls._totalAnimales = totalAnimales    

    def getNombre(self):
        return self._nombre

    def setNombre(self,nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad

    def setEdad(self,edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat

    def setHabitat(self,habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero

    def setGenero(self,genero):
        self._genero = genero

    def getZonas(self):
        return self._zonas

    def setZonas(self,zonas):
        self._zonas = zonas