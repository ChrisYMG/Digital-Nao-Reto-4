def nombre_de_unidad(numero):
    unidades = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    especiales = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
    if numero < 10:
        return unidades[numero]
    elif numero < 20:
        return especiales[numero - 10]
    else:
        decenas = ["veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
        if numero % 10 == 0:
            return decenas[numero // 10 - 2]
        elif numero < 30:
            return "veinti" + unidades[numero % 10]
        else:
            return decenas[numero // 10 - 2] + " y " + unidades[numero % 10]

def numero_a_palabra(numero):
    if numero < 100:
        return nombre_de_unidad(numero)
    elif numero == 100:
        return "cien"
    else:
        centenas = ["ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]
        if numero < 1000:
            parte_centena = centenas[numero // 100 - 1]
            parte_resto = nombre_de_unidad(numero % 100)
            if numero % 100 == 0:
                return parte_centena
            else:
                return parte_centena + " " + parte_resto

# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número entre 0 y 999: "))
print(numero_a_palabra(numero))