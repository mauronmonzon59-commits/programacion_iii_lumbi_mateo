# operadores 
"""

operadores aritméticos: 
+,
-,
*,
/,
//,
%,
**
"""
valor1 = 10
valor2 = 3
suma = valor1 + valor2
resta = valor1 - valor2
multiplicacion = valor1 * valor2
division = valor1 / valor2
modulo = valor1 % valor2
potencia = valor1 ** valor2

print("Suma: ", suma)
print("Resta: ", resta)
print("Multiplicación: ", multiplicacion)
print("División: ", division)
print("Módulo: ", modulo)
print("Potencia: ", potencia)

print("tabla de multiplicar del 5")
print("5 x 1 = ", 5 * 1)
print("5 x 2 = ", 5 * 2)
print("5 x 3 = ", 5 * 3)
print("5 x 4 = ", 5 * 4)
print("5 x 5 = ", 5 * 5)


#operadores de comparacion
"""
- == (igual)
- != (distinto)
- < (menor)
- > (mayor)
- <= (menor o igual)
- >= (mayor o igual)
"""
velocidad_aniki = 950
velocidad_sebula = 900

print("¿anaki es más rápido que sebula? ", velocidad_aniki > velocidad_sebula)
print("¿anaki es más lento que sebula? ", velocidad_aniki < velocidad_sebula)
print("¿anaki es igual a sebula? ", velocidad_aniki == velocidad_sebula)
print("¿anaki es distinto a sebula? ", velocidad_aniki != velocidad_sebula)
print("¿anaki es mayor o igual a sebula? ", velocidad_aniki >= velocidad_sebula)
print("¿anaki es menor o igual a sebula? ", velocidad_aniki <= velocidad_sebula)
print("¿anaki es mayor o igual a sebula? ", velocidad_aniki >= velocidad_sebula)

resultado = velocidad_aniki > velocidad_sebula
print("Resultado de la comparación: ", resultado)
print("Tipo de dato de la comparación: ", type(resultado))


#operadores logicos
"""
- and (y)
- or (o)
- not (no)
"""

motores_funcionando = True
escudos_funcionando = False
combustible = 80

print("¿todos los sistemas están funcionando? ", motores_funcionando and escudos_funcionando)
print("¿algunos sistemas están funcionando? ", motores_funcionando or escudos_funcionando)
print("¿los motores no están funcionando? ", not motores_funcionando)

cantidad_motores = 2
cantidad_alas = 4
combustible = 80
print("¿la nave tiene al menos 2 motores y 4 alas? ", cantidad_motores >= 2 and cantidad_alas >= 4)
print("¿la nave tiene al menos 2 motores o 4 alas? ", cantidad_motores >= 2 or cantidad_alas >= 4)
print("¿la nave no tiene al menos 2 motores? ", not cantidad_motores >= 2)





# operadores de asignación














# presedencia de operadores 
"""
1. ()
2. **
3. *, /, %
4. +, -
"""
resultado = 10 + 5 * 2
print("resultado 1: ", resultado)
resultado_2 = (10 + 5) * 2
print("resultado 2: ", resultado_2)