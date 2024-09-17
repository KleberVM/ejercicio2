#Desarrollado por Yahir Leonardo Cayola Cayo 
def division(numerador, denominador):
    try:
        resultado = numerador / denominador
        return f"El resultado de la división es: {resultado}"
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero."
    except TypeError:
        return "Error: Los valores deben ser números."
