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
    
jedi = {}

jedi_activo = {"nombre": " obiwan",
               "fuerza": 120,
               "estilo_pelea": "samaurai",
               "misiones": ["querra alderan", "secuestro palpante", "escolta de laia"],
               "descripcion": {"estatura": 1.80, "espeie": "humana",}
                }
print("jedi activo")
nave = dict(nombre="AZ-1", capacidad=8, turbo_laser=2)
print(nave)



jedi["nombre"] = "luck"
jedi["fuerza"] = 150
print(jedi)

for calve, valor in jedi_activo.items():
    print(f"{calve}: {valor}")