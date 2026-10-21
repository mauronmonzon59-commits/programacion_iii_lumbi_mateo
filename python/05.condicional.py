combustible = 10
if combustible >= 10:
    print("puedes despegar")
    
# condicional if else
credito = int(input("ingresa tu credito: "))

precio_repuesto = int(input("ingresa el precio del repuesto: "))
if credito >= precio_repuesto:
    print("puedes comprar el repuesto")
else:
    print("no puedes comprar el repuesto")
    
#if anidado
if credito >= precio_repuesto:
    print("puedes comprar el repuesto")
    if credito > precio_repuesto:
        print("te sobra dinero")
    else:
        print("no te sobra dinero")
else:
    print("no puedes comprar el repuesto")
    
# condicional if elif else
if credito >= precio_repuesto:
    print("puedes comprar el repuesto")
elif credito == precio_repuesto:
    print("te sobra dinero")
else:
    print("no te sobra dinero")
    