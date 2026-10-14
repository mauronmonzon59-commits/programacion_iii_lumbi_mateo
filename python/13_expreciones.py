print("===== CONTROL DE ENERGIA ===0")
energia_texto = "ochenta"
try:
    energia = int(energia_texto)
    print(energia)
except ValueError:
    print("error : debe ser numerico")

print("find del sismeta ")




"""
ValueError
TypeError
KeyError
IndexError
ZeroDivisionError
"""

def calcular_energia(total, cantidad):
    try:
        resultado = total / cantidad
    except ZeroDivisionError:
        print("error: division entre cero")
        return None
    except TypeError:
        print("error: valores deden ser numericos")
        return None
print("caso 1:", calcular_energia(100,4))
print("caso 2:", calcular_energia(100,0))
print("caso 3:", calcular_energia(100,"cuatro"))


print("=====DIAGNOSTICO R2-D2 ======0")
try:
    energia = int(90)
    print("energia", energia)
except ValueError:
    print("Error de lectura")
else:
    print("diagnostico completado")
finally:
    print("Cerrando diagnostico")


def validar_enegia(energia):
    if type(energia) is not int:
        raise TypeError("la energia debe ser numero entero")
    if energia <0 or energia >100:
        raise TypeError("la energia debe estar entre 0 y 100")
    return energia
try:
    resultado = validar_enegia(150)
    print("energia", resultado)
except (TypeError,ValueError) as error:
    print("Error:", error)
    