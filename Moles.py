isG = print("La unidad de medida del soluto son Kg? y/n")
gSoluto = float(input("Digite los gramos de soluto: "))
PM = float(input("Digite el peso molecular: "))
if (isG == "y" or isG == "Y"): gKg = gSoluto; gSoluto = (gSoluto*1)/1000
N = (gSoluto/PM)

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