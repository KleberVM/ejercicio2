#Desarrollado por Yahir Leonardo Cayola Cayo
def dividir():
    num1 = int(input("ingrese el 1er numero a sumar: "))
    num2 = int(input("ingrese el 2do numero a sumar : "))
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: No se puede dividir entre cero."
