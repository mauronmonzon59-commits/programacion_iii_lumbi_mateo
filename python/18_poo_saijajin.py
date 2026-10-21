from  _poo_guerrero import Guerrero

class Saiyajin(Guerrero):
    def transformarse(self):
        print(f"{self.nombre} se ha transformado en Saiyajin!")

goku = Saiyajin("Goku")
goku.presentarse()
goku.transformarse()