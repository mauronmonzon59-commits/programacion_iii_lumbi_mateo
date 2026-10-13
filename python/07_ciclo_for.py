#ciclo for 
naves = ["caza N-1",
         "Nave real del naboo",
         "transporte"]

for nave in naves:
    print("inspeccionando", nave)
    
print("inspeccion completa")

droides = range(1, 17, 6)

print("tipo de rondas: ", type(droides))
for droides in droides:
    print(f"reparar :droide b1- {droides}")
    print(f"tipo de dato de droide : {type(droides)}")
    
    
planetas = ["Naboo", "Coruscant", "Tatooine" ]
recorrido  = enumerate(planetas, start=1)

for posicion, planeta in recorrido:
    print(f"destino {posicion}: {planeta}")
    print(f"tipo de dato : {type(posicion)}: {type(planeta)}")
    
paises = ["ecuador", "venezuela", "chile", "brasil", "estados unidos"]

for pais in paises:
    if pais == "chile":
        continue
    if pais == "brasil":
        break
    print(f"pais visitado: {pais}")
    
        