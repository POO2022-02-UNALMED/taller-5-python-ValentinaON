from zooAnimales.animal import Animal
class Mamifero(Animal):
    caballos = 0
    leones = 0
    _listado=[]

    def __init__(self, nombre, edad, habitat, genero, zona, pelaje, patas):
        if zona != None:
            super.__init__(nombre,edad,habitat,genero,zona)
            self._pelaje = pelaje
            self._patas = patas
            Mamifero._listado.append(self)
        else:
            super.__init__(nombre,edad,habitat,genero)
            self._pelaje = pelaje
            self._patas = patas
            Mamifero._listado.append(self)

    @classmethod
    def cantidadMamiferos(cls):
        if cls._listado != None:
            return len(cls._listado)
        else:
            return 0


    @classmethod
    def crearCaballo(cls,nombre,edad,genero):
        caballo = cls(nombre, edad, "pradera", genero, True, 4)
        cls._listado.append(caballo)
        cls.caballos += 1
        return caballo

    @classmethod
    def crearLeon(cls,nombre,edad,genero):
        leon = cls(nombre, edad, "selva", genero, True, 4)
        cls._listado.append(leon)
        cls.leones += 1
        return leon

    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def setListado(cls, listado):
        cls._listado = listado

    def isPelaje(self):
        return self._pelaje
    
    def setPelaje(self, pelaje):
        self._pelaje = pelaje

    def getPatas(self):
        return self._patas
    
    def setPatas(self, patas):
        self._patas = patas