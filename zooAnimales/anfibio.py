from zooAnimales.animal import Animal
class Anfibio(Animal):
    ranas = 0
    salamandras = 0
    _listado=[]

    def __init__(self, nombre, edad, habitat, genero, zona, colorPiel, venenoso):
        if zona != None:
            super.__init__(nombre,edad,habitat,genero,zona)
            self._colorPiel = colorPiel
            self._venenoso = venenoso
            Anfibio._listado.append(self)
        else:
            super.__init__(nombre,edad,habitat,genero)
            self._colorPiel = colorPiel
            self._venenoso = venenoso
            Anfibio._listado.append(self)

    @classmethod
    def cantidadAnfibios(cls):
        if cls._listado != None:
            return len(cls._listado)
        else:
            return 0

    def movimiento():
        return "saltar"

    @classmethod
    def crearRana(cls,nombre,edad,genero):
        rana = cls(nombre,edad,"selva",genero,"rojo",True)
        cls._listado.append(rana)
        cls.ranas += 1
        return rana

    @classmethod
    def crearSalamandra(cls,nombre,edad,genero):
        salamandra = cls(nombre,edad,"selva",genero,"negro y amarilli",False)
        cls._listado.append(salamandra)
        cls.salamandras += 1
        return salamandra

    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def setListado(cls, listado):
        cls._listado = listado

    def getColorPiel(self):
        return self._colorPiel
    
    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    def isVenenoso(self):
        return self._venenoso

    def setVenenoso(self, venenoso):
        self._venenoso = venenoso


    