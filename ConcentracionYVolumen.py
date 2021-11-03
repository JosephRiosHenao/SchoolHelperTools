print("V1 x C1 = V2 x C2")
X = input("Cual es su incognita? (V/C): ").upper()
while (X != "V" and X != "C"):
    X = input("Cual es su incognita? (V/C): ").upper()

if (X == "V"):
    V1 = float(input("Digite el valor de V1: "))
    C1 = float(input("Digite el valor de C1: "))
    C2 = float(input("Digite el valor de C2: "))
    V2 = (V1*C1)/C2
    print("V2 = (V1 x C1)/C2")
    print("V2 = ",(V1+C1),"/",C2)
    print("V2 = ",V2)
if (X == "C"):
    V1 = float(input("Digite el valor de V1: "))
    C1 = float(input("Digite el valor de C1: "))
    V2 = float(input("Digite el valor de V2: "))
    C2 = (V1*C1)/V2
    print("C2 = (V1 x C1)/V2")
    print("C2 = (",V1,"x",C1)
    print("C2 = ",(V1+C1),"/",V2)
    print("C2 = ",C2)