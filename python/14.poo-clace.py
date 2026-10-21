class guerrero:
    nombre : str
    poder: int
    def __init__(self,nombre: str, poder:int):
        
        self.nombre = nombre
        self.poder = poder
        
    def saludar(self):
        print("hola,soy:", self.nombre)
    
    
    def entrenar(self):
        aumento = 200
        self.poder+= aumento
    
    def atacar(self,cantidad):
        danio = self.poder*cantidad
        print("guerrero",self.nombre)
        print("daño causado:", danio)
        
        
goku = guerrero("goku",9000)
goku.saludar()

print("nombre del personaje:", goku.nombre)
print("poder del personaje:", goku.poder)
goku.entrenar()
print("poder del personaje",goku.poder)

goku.atacar(3)






class RadarDragon:
    def __init__(self, region1, region2):
        self.region1 = region1
        self.region2 = region2

    def buscar_esferas(self):
        encontradas = self.region1 + self.region2
        faltan = 7 - encontradas

        return encontradas, faltan


radar_bulma = RadarDragon(3, 2)


encontradas, faltan = radar_bulma.buscar_esferas()

print("Esferas encontradas:", encontradas)
print("Esferas que faltan:", faltan)