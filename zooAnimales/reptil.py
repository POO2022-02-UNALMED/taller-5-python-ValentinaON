from zooAnimales.animal import Animal
class Reptil(Animal):
    iguanas = 0
    serpientes = 0
    _listado=[]

    def __init__(self, nombre, edad, habitat, genero, zona, colorEscamas, largoCola):
        if zona != None:
            super.__init__(nombre,edad,habitat,genero,zona)
            self._colorEscamas = colorEscamas
            self._largoCola = largoCola
            Reptil._listado.append(self)
        else:
            super.__init__(nombre,edad,habitat,genero)
            self._colorEscamas = colorEscamas
            self._largoCola = largoCola
            Reptil._listado.append(self)

    @classmethod
    def cantidadReptiles(cls):
        if cls._listado != None:
            return len(cls._listado)
        else:
            return 0

    def movimiento():
        return "reptar"

    @classmethod
    def crearIguana(cls,nombre,edad,genero):
        iguana = cls(nombre, edad, "humedal", genero, "verde",3)
        cls._listado.append(iguana)
        cls.iguanas += 1
        return iguana

    @classmethod
    def crearSerpiente(cls,nombre,edad,genero):
        serpiente = cls(nombre, edad, "jungla", genero, "blanco",1)
        cls._listado.append(serpiente)
        cls.serpientes += 1
        return serpiente

    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def setListado(cls, listado):
        cls._listado = listado

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCola(self, largoCola):
        self._largoCola = largoCola