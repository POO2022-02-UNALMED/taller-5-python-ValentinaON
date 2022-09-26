from zooAnimales.animal import Animal
class Ave(Animal):
    halcones = 0
    aguilas = 0
    _listado=[]

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super.__init__(nombre,edad,habitat,genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)
     
    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)
       
    def movimiento():
        return "volar"

    @classmethod
    def crearHalcon(cls,nombre,edad,genero):
        cls.halcones += 1
        return cls(nombre, edad, "montanas", genero, "cafe glorioso")

    @classmethod
    def crearAguila(cls,nombre,edad,genero):
        cls.aguilas += 1
        return cls(nombre, edad, "montanas", genero, "blanco y amarillo")

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

