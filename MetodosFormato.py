cadena = "bienvEnido a mi aplicAción"

print("primera mayuscula")
print(cadena.capitalize())

print("convierte minuscula")
print(cadena.lower())

print("convierte mayuscula")
print(cadena.upper())

print("Convierte may a minusculas y visiversa")
print(cadena.swapcase())

print("Convierte el texto a las primeras letras en mayusculas")
print(cadena.title())


#CARACTER DE RELLENO
cadena1 = "Eliacer Fernandez".title()
print(cadena1.center(50, "-") )

print(cadena1.ljust(50, "="))

print(cadena1.rjust(50, "="))


numero = 5678
print(str(numero).zfill(7))