class guerrero:
    nombre: str

    def __init__(self, nombre: str):
        self.nombre = nombre

    def presentarse(self):
        print("Mi poderoso nombre es", self.nombre)


class saiyajin(guerrero):
    def __init__(self, nombre: str):
        super().__init__(nombre)

    def trasformarse(self):
        print(self.nombre, "se transforma en Super Saiyajin")


goku = saiyajin("Goku")

goku.presentarse()
goku.trasformarse()


class androide:
    nombre: str
    energia: int

    def __init__(self, nombre: str, energia: int):
        self.nombre = nombre
        self.energia = energia

    def mostrar_energia(self):
        print("Androide:", self.nombre)
        print("Energia:", self.energia)


class androiderecargable(androide):
    def __init__(self, nombre: str, energia: int):
        super().__init__(nombre, energia)

    def recargar(self, cantidad: int):
        if cantidad > 0:
            self.energia += cantidad
            print("Recarga realizada:", cantidad)
        else:
            print("Cantidad no permitida")


androide17 = androiderecargable("Numero 17", 600)

print("====== antes de recarga ======")
androide17.mostrar_energia()

androide17.recargar(200)

print("====== despues de recargar ======")
androide17.mostrar_energia()