def dividir():
    try:
        numerador = float(input("Ingresa el numerador: "))
        denominador = float(input("Ingresa el denominador: "))
        resultado = numerador / denominador
        print(f"El resultado de la división es: {resultado}")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except ValueError:
        print("Error: Debes ingresar valores numéricos.")

# Ejecutar el programa
dividir()
