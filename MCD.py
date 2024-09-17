#Realizado por Orlando Altamirano Vargas
def mcd():
    # Solicitar al usuario que ingrese dos números
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))

    # Calcular el MCD utilizando el algoritmo de Euclides
    while num2:
        num1, num2 = num2, num1 % num2
    
    # Retornar el resultado
    return num1