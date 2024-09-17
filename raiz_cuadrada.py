# Realizado por Yamil Angelo Lara Balderrama
def calcular_raiz():
    num = float(input("Ingresa un numero: "))
    
    if num < 0:
        return "No se puede calcular la raiz cuadrada de un numero negativo"
    else:
        return math.sqrt(num)