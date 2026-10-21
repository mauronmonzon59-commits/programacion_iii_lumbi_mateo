

print("logistica internacional")
print("precio del paquete")
paquete = float(input("peso del paquete en kilogramos: "))
print("seleccione la zona de destino solo numero")
print("zona 1: 5.0 por kilo")
print("zona 2: 7.5 por kilo")
print("zona 3: 10.0 por kilo")  
zona = int(input("zona: "))

if zona == 1:
    print("el precio es 5.0 por kilo")
elif zona == 2:
    print("el precio es 7.5 por kilo")
elif zona == 3:
    print("el precio es 10.0 por kilo")
else:
    print("zona no valida")


