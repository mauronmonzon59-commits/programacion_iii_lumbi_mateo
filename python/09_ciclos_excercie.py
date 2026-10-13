"""
CONTROL DE FLOTA de naboo
"""

naves = [{
    "nombre": "caza N-1",
    "combustible": 80,
    "droides": ["R2-D2", "r2-a6"]
}]

naves = [{
    "nombre": "caza REAL",
    "combustible": 35,
    "droides": ["R2-N3"]
}]

naves = [{
    "nombre": "TRASNPORTE",
    "combustible": 65,
    "droides": ["R2-D2", "R2-A6"]
}]


naves_listas = 0
naves_recargadas = 0
total_droides = 0
total_ciclos = 0
for numero, nave in enumerate(naves, start=1):
    print(f"---- nave: {numero} - {nave}")
    if nave["combustible"] >= 50:
        print(" estado inicial: lista")
        naves_listas += 1
    else:
        print(" estado inicial: recargar")
        naves_recargadas += 1
        ciclo = 0 
        while nave["combustible"] <= 50:
            ciclo += 1
            nave["combustible"] += 10
        total_ciclos += ciclo
        print("recarga completa")
        print("estado final: lista")
    total_droides += len(nave["droides"])
    for droide in nave["droides"]:
        print(f"doride: {droide}")
        
print("=======================")
print("resumen")
print("=======================")
print(f"total de naves: {len(nave)}")
print(f"naves listas inicialmente: {naves_listas}")
print(f"naves que necesitaron recarga: {naves_recargadas}")
print(f"total de ciclos de recarga: {total_ciclos}")
print(f"total de droides: {total_droides}")