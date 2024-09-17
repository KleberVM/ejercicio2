from multiplicar import multiplicar
# from division import dividir
# from Raiz Cuadrada import calcular_raiz


operacion = input("ingrese una de las siguientes operaciones: + , - , * , / , % , potencia , sqrt , exit: ")


while operacion != "exit":

    if operacion == "*":
        resultado = multiplicar()
    
    # elif operacion == "/":
    #     resultado = dividir()        

    # elif operacion == "sqrt":
    #     resultado = calcular_raiz()

    print(f"el resultado de la operacion es: {resultado}")
    operacion = input("ingrese una de las siguientes opciones: + , - , * , / , % , potencia , sqrt , exit: ")

