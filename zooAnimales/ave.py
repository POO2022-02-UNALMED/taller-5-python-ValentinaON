from zooAnimales.animal import Animal
class Ave(Animal):
    halcones = 0
    aguilas = 0
    _listado=[]

    def __init__(self, nombre, edad, habitat, genero, zona, colorPlumas):
        super.__init__(nombre,edad,habitat,genero,zona)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    @classmethod
    def cantidadAves(cls):
        if cls._listado != None:
            return len(cls._listado)
        else:
            return 0

    def movimiento():
        return "volar"

    @classmethod
    def crearHalcon(cls,nombre,edad,genero):
        halcon = cls(nombre, edad, "montanas", genero, "cafe glorioso")
        cls._listado.append(halcon)
        cls.halcones += 1
        return halcon

    @classmethod
    def crearAguila(cls,nombre,edad,genero):
        aguila = cls(nombre, edad, "montanas", genero, "blanco y amarillo")
        cls._listado.append(aguila)
        cls.aguilas += 1
        return aguila

    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def setListado(cls, listado):
        cls._listado = listado

    def getColorPlumas(self):
        return self._colorPiel
    
    def setColorPlumas(self, colorPiel):
        self._colorPiel = colorPiel

