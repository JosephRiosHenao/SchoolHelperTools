isL = input("Su unidad de solucion esta en litros? y/n: ")
solucion = float(input("Digite su solucion: "))
if (isL == "n" or isL == "N"): mlSolucion = solucion; solucion = ((solucion * 1)/1000)

isG = print("La unidad de medida del soluto son Kg? y/n")
gSoluto = float(input("Digite los gramos de soluto: "))
if (isG == "y" or isG == "Y"): gKg = gSoluto; gSoluto = (gSoluto*1)/1000

PM = float(input("Digite su peso molecular: "))
N = (gSoluto/PM)
n = (N/solucion)


if (isL == "n" or isL == "N"):
    print("Pasamos la solucion de mL a L")
    print("1L / 1000mL  x  ",mlSolucion,"ml / X")
    print("X = ",mlSolucion," / 1000")
    print("X = ",mlSolucion)
if (isG == "y" or isG == "Y"):
    print("Pasamos el soluto de Kg a G")
    print("1Kg / 1000g  x  ",gKg,"g / X")
    print("X = ",gKg," / 1000")
    print("X = ",gKg)


print("Hallamos los moles")
print("N = gramos de soluto / peso molecular")
print("N = ",gSoluto," / ",PM)
print("N = ",N," N")
print("Los moles son ",N," N")

print("n = moles de soluto / solucion en litros")
print("n = N / gSolucion")
print("n = ",N," / ",solucion)
print("n = ",n)
print("La molaridad es: ",n," n")