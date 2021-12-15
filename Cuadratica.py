import math
values = {"a" : 0, "b" : 0, "c" : 0, "D" : 0, "Xpos" : 0, "Xneg" : 0}
values["a"] = float(input("Digite el valor de a (cuadrado): "))
values["b"] = float(input("Digite el valor de b (elevado): "))
values["c"] = float(input("Digite el valor de c (independiente): "))
values["D"] = ((values["b"]**2)+(-4*values["a"]*values["c"]))
if (values["D"]>0): 
    values["Xpos"] = ((-1*(values["b"])) + math.sqrt(values["D"])) / (2*values["a"]) 
    values["Xneg"] = ((-1*(values["b"])) - math.sqrt(values["D"])) / (2*values["a"])
    print(values["Xpos"]," - ",values["Xneg"])
else: print("La ecuacion no tiene soluciones reales")