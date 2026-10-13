## funciones 
def activar_sistema():
    print("== sistema de naboo")
    print("sistema de control de activado")

activar_sistema()

#funciones com parametros 
def saludar_jedi(nombre):
    print("que la fuerza te acompañe: {nombre}")
saludar_jedi("quin-gon jim")
saludar_jedi("obi-wan kwnobi")


def mostrar_nave(nombre, combustible):
    print(f"nave": {nombre})
    print(f"cantidad combustible : {combustible}")
mostrar_nave("caza n-1",80)

#funciones que devuvlven dato o informacion 
#return

def calcular_combustible(inicial, consumo):
    restante = inicial - consumo
    return(restante)
resultado = calcular_combustible(100.25)
print(f"combustible: {resultado}")
